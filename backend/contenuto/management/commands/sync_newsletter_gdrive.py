"""
Sincronizza iscritti newsletter da un file Excel/CSV su Google Drive.

Variabili d'ambiente richieste:
  GDRIVE_SERVICE_ACCOUNT_JSON  – contenuto JSON del service account (stringa)
  GDRIVE_FILE_ID               – ID del file su Google Drive
"""
import io
import csv
import json
import os

from django.core.management.base import BaseCommand
from django.db import transaction


def _download_file(file_id: str, sa_info: dict) -> tuple[bytes, str]:
    """Scarica il file da Drive e restituisce (contenuto, nome_file)."""
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaIoBaseDownload
    from google.oauth2.service_account import Credentials

    creds = Credentials.from_service_account_info(
        sa_info,
        scopes=["https://www.googleapis.com/auth/drive.readonly"],
    )
    service = build("drive", "v3", credentials=creds, cache_discovery=False)

    meta = service.files().get(fileId=file_id, fields="name,mimeType").execute()
    filename = meta["name"]
    mime = meta["mimeType"]

    if "spreadsheet" in mime:
        # Google Sheets → esporta come CSV
        content = service.files().export(fileId=file_id, mimeType="text/csv").execute()
        filename = filename + ".csv"
    else:
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, service.files().get_media(fileId=file_id))
        done = False
        while not done:
            _, done = downloader.next_chunk()
        content = fh.getvalue()

    return content, filename


def _parse(content: bytes, filename: str) -> list[dict]:
    """Parsa CSV o Excel e restituisce lista di dict con chiavi normalizzate."""
    if filename.lower().endswith((".xlsx", ".xls")):
        return _parse_excel(content)
    return _parse_csv(content)


def _parse_csv(content: bytes) -> list[dict]:
    for enc in ("utf-8-sig", "utf-8", "latin-1"):
        try:
            text = content.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    reader = csv.DictReader(io.StringIO(text))
    return [_normalize(row) for row in reader]


def _parse_excel(content: bytes) -> list[dict]:
    import openpyxl
    wb = openpyxl.load_workbook(io.BytesIO(content), read_only=True, data_only=True)
    ws = wb.active
    rows = list(ws.iter_rows(values_only=True))
    if not rows:
        return []
    headers = [str(h or "").lower().strip() for h in rows[0]]
    result = []
    for row in rows[1:]:
        raw = {headers[i]: str(v or "").strip() for i, v in enumerate(row) if i < len(headers)}
        result.append(_normalize(raw))
    return result


# Mappatura colonne comuni → chiavi standard
_COL_MAP = {
    "email": "email",
    "e-mail": "email",
    "e_mail": "email",
    "indirizzo email": "email",
    "mail": "email",
    "nome": "nome",
    "first name": "nome",
    "firstname": "nome",
    "name": "nome",
    "cognome": "cognome",
    "last name": "cognome",
    "lastname": "cognome",
    "surname": "cognome",
}


def _normalize(row: dict) -> dict:
    out = {}
    for k, v in row.items():
        std = _COL_MAP.get(k.lower().strip())
        if std:
            out[std] = v
    return out


def run_sync(file_id: str, sa_json_str: str) -> dict:
    """
    Esegue la sync e restituisce un dict con i contatori.
    Chiamabile sia dal management command che dalla view admin.
    """
    from contenuto.models import NewsletterIscritto

    sa_info = json.loads(sa_json_str)
    content, filename = _download_file(file_id, sa_info)
    rows = _parse(content, filename)

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

    return {
        "filename": filename,
        "total": len(rows),
        "created": created,
        "updated": updated,
        "skipped": skipped,
        "errors": errors,
    }


class Command(BaseCommand):
    help = "Sincronizza iscritti newsletter da un file CSV/Excel su Google Drive"

    def handle(self, *args, **options):
        sa_json = os.environ.get("GDRIVE_SERVICE_ACCOUNT_JSON", "")
        file_id = os.environ.get("GDRIVE_FILE_ID", "")

        if not sa_json or not file_id:
            self.stdout.write(self.style.ERROR(
                "Variabili mancanti: GDRIVE_SERVICE_ACCOUNT_JSON e GDRIVE_FILE_ID"
            ))
            return

        self.stdout.write("Connessione a Google Drive...")
        result = run_sync(file_id, sa_json)

        self.stdout.write(f"  File: {result['filename']}")
        self.stdout.write(f"  Righe lette: {result['total']}")
        self.stdout.write(self.style.SUCCESS(
            f"  Nuovi: {result['created']} · Aggiornati: {result['updated']} · Saltati: {result['skipped']}"
        ))
        if result["errors"]:
            for err in result["errors"]:
                self.stdout.write(self.style.WARNING(f"  ⚠ {err}"))
