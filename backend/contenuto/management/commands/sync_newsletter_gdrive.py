"""
Sincronizza iscritti newsletter da Google Drive.

Naming convention attesa: iscritti_newsletter_YYYYMMDD.csv
I file processati vengono spostati in sync_archive/<YYYYMMDD>/

Variabili d'ambiente richieste:
  GDRIVE_FOLDER_ID                – ID della cartella Drive da monitorare
  GDRIVE_SERVICE_ACCOUNT_JSON     – JSON del service account (stringa)
  oppure
  GDRIVE_SERVICE_ACCOUNT_FILE     – percorso al JSON del service account
"""
import csv
import io
import json
import os
import re

from django.core.management.base import BaseCommand
from django.db import transaction

FILE_PATTERN = re.compile(r"^iscritti_newsletter_(\d{8})\.csv$")
SCOPES = ["https://www.googleapis.com/auth/drive"]


# ── Credenziali ───────────────────────────────────────────────────────────────

def _load_sa_info() -> dict:
    sa_json = os.environ.get("GDRIVE_SERVICE_ACCOUNT_JSON", "")
    if sa_json:
        return json.loads(sa_json)
    sa_file = os.environ.get("GDRIVE_SERVICE_ACCOUNT_FILE", "")
    if sa_file:
        with open(sa_file) as f:
            return json.load(f)
    raise Exception("GDRIVE_SERVICE_ACCOUNT_JSON o GDRIVE_SERVICE_ACCOUNT_FILE richiesto")


def _build_service(sa_info: dict):
    from googleapiclient.discovery import build
    from google.oauth2.service_account import Credentials
    creds = Credentials.from_service_account_info(sa_info, scopes=SCOPES)
    return build("drive", "v3", credentials=creds, cache_discovery=False)


# ── Operazioni su Drive ───────────────────────────────────────────────────────

def _get_or_create_folder(service, name: str, parent_id: str) -> str:
    """Restituisce l'ID di una sottocartella, creandola se non esiste."""
    q = (
        f"name='{name}' "
        f"and mimeType='application/vnd.google-apps.folder' "
        f"and '{parent_id}' in parents "
        f"and trashed=false"
    )
    results = service.files().list(q=q, fields="files(id)", pageSize=1).execute()
    files = results.get("files", [])
    if files:
        return files[0]["id"]
    folder = service.files().create(
        body={"name": name, "mimeType": "application/vnd.google-apps.folder", "parents": [parent_id]},
        fields="id",
    ).execute()
    return folder["id"]


def _find_newsletter_files(service, folder_id: str) -> list[dict]:
    """Trova i file che rispettano la naming convention nella cartella."""
    q = f"'{folder_id}' in parents and trashed=false"
    results = service.files().list(q=q, fields="files(id,name)", pageSize=100).execute()
    matches = []
    for f in results.get("files", []):
        m = FILE_PATTERN.match(f["name"])
        if m:
            matches.append({"id": f["id"], "name": f["name"], "date": m.group(1)})
    return sorted(matches, key=lambda x: x["date"])


def _download_content(service, file_id: str) -> bytes:
    from googleapiclient.http import MediaIoBaseDownload
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, service.files().get_media(fileId=file_id))
    done = False
    while not done:
        _, done = downloader.next_chunk()
    return fh.getvalue()


def _archive_file(service, file_id: str, date_str: str, source_folder_id: str, archive_root_id: str):
    """Sposta il file in sync_archive/<date_str>/."""
    date_folder_id = _get_or_create_folder(service, date_str, archive_root_id)
    service.files().update(
        fileId=file_id,
        addParents=date_folder_id,
        removeParents=source_folder_id,
        fields="id,parents",
    ).execute()


# ── Parsing CSV ───────────────────────────────────────────────────────────────

_COL_MAP = {
    "email": "email", "e-mail": "email", "e_mail": "email",
    "indirizzo email": "email", "mail": "email",
    "nome": "nome", "first name": "nome", "firstname": "nome", "name": "nome",
    "cognome": "cognome", "last name": "cognome", "lastname": "cognome", "surname": "cognome",
}


def _normalize(row: dict) -> dict:
    return {_COL_MAP[k.lower().strip()]: v for k, v in row.items() if k.lower().strip() in _COL_MAP}


def _parse_csv(content: bytes) -> list[dict]:
    for enc in ("utf-8-sig", "utf-8", "latin-1"):
        try:
            text = content.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    reader = csv.DictReader(io.StringIO(text))
    return [_normalize(row) for row in reader]


# ── Upsert nel DB ─────────────────────────────────────────────────────────────

def _upsert_rows(rows: list[dict]) -> dict:
    from contenuto.models import NewsletterIscritto
    created = updated = skipped = 0
    errors = []
    with transaction.atomic():
        for row in rows:
            email = row.get("email", "").strip().lower()
            if not email:
                skipped += 1
                continue
            nome = row.get("nome", "").strip()
            cognome = row.get("cognome", "").strip()
            try:
                obj, was_created = NewsletterIscritto.objects.get_or_create(
                    email=email,
                    defaults={"nome": nome, "cognome": cognome, "attivo": True},
                )
                if was_created:
                    created += 1
                else:
                    changed = False
                    if nome and obj.nome != nome:
                        obj.nome = nome
                        changed = True
                    if cognome and obj.cognome != cognome:
                        obj.cognome = cognome
                        changed = True
                    if changed:
                        obj.save(update_fields=["nome", "cognome"])
                        updated += 1
                    else:
                        skipped += 1
            except Exception as e:
                errors.append(f"{email}: {e}")
    return {"created": created, "updated": updated, "skipped": skipped, "errors": errors}


# ── Entry point ───────────────────────────────────────────────────────────────

def run_sync(folder_id: str) -> dict:
    """
    Processa tutti i file iscritti_newsletter_YYYYMMDD.csv nella cartella,
    li importa nel DB e li sposta in sync_archive/<YYYYMMDD>/.
    """
    sa_info = _load_sa_info()
    service = _build_service(sa_info)

    files = _find_newsletter_files(service, folder_id)
    if not files:
        return {
            "files": [],
            "created": 0, "updated": 0, "skipped": 0, "errors": [],
            "message": "Nessun file iscritti_newsletter_YYYYMMDD.csv trovato nella cartella.",
        }

    archive_root_id = _get_or_create_folder(service, "sync_archive", folder_id)

    total = {"created": 0, "updated": 0, "skipped": 0, "errors": []}
    processed = []

    for f in files:
        content = _download_content(service, f["id"])
        rows = _parse_csv(content)
        result = _upsert_rows(rows)

        total["created"] += result["created"]
        total["updated"] += result["updated"]
        total["skipped"] += result["skipped"]
        total["errors"] += result["errors"]

        _archive_file(service, f["id"], f["date"], folder_id, archive_root_id)
        processed.append({"name": f["name"], "date": f["date"], "rows": len(rows)})

    return {
        "files": processed,
        "created": total["created"],
        "updated": total["updated"],
        "skipped": total["skipped"],
        "errors": total["errors"],
    }


class Command(BaseCommand):
    help = "Sincronizza newsletter da file iscritti_newsletter_YYYYMMDD.csv su Google Drive"

    def handle(self, *args, **options):
        folder_id = os.environ.get("GDRIVE_FOLDER_ID", "")
        if not folder_id:
            self.stdout.write(self.style.ERROR("GDRIVE_FOLDER_ID non configurato"))
            return

        self.stdout.write("Connessione a Google Drive...")
        result = run_sync(folder_id)

        if not result["files"]:
            self.stdout.write(self.style.WARNING(result.get("message", "Nessun file trovato")))
            return

        for f in result["files"]:
            self.stdout.write(f"  ✓ {f['name']}  ({f['rows']} righe) → sync_archive/{f['date']}/")

        self.stdout.write(self.style.SUCCESS(
            f"\nTotale: {result['created']} nuovi · {result['updated']} aggiornati · {result['skipped']} saltati"
        ))
        for err in result["errors"]:
            self.stdout.write(self.style.WARNING(f"  ⚠ {err}"))
