"""
Assegna foto profilo ai medici in base al sesso inferito dal nome.
Usa ritratti da randomuser.me — URL stabili, tutti diversi.

Uso:
    python manage.py update_medici_foto           # solo medici senza foto
    python manage.py update_medici_foto --force   # sovrascrive tutti
"""
from django.core.management.base import BaseCommand
from prestazioni.models import Struttura  # solo per import check
from contenuto.models import SchedaMedico

# Pool di 20 ritratti femminili e 20 maschili da randomuser.me
# URL formato: https://randomuser.me/api/portraits/{women|men}/{n}.jpg
FOTO_DONNE = [f"https://randomuser.me/api/portraits/women/{n}.jpg"
              for n in [2, 5, 9, 14, 17, 21, 26, 33, 38, 44,
                        51, 57, 62, 65, 71, 76, 82, 87, 91, 96]]

FOTO_UOMINI = [f"https://randomuser.me/api/portraits/men/{n}.jpg"
               for n in [3, 7, 11, 16, 22, 28, 35, 41, 47, 53,
                         58, 63, 68, 74, 79, 84, 88, 93, 97, 99]]

# Nomi italiani maschili che terminano in 'a' (eccezioni alla regola)
MASCHILI_IN_A = {
    "luca", "andrea", "nicola", "mattia", "danila", "enea",
    "battista", "tobia", "elia", "costa", "gianluca", "pierluigi",
}

TITOLI = {"dott.", "dott.ssa", "dottssa", "prof.", "prof.ssa", "dr.", "dr", "dott", "prof"}


def _inferisci_sesso(nome_completo: str) -> str:
    """Restituisce 'f' o 'm' in base al primo nome, saltando i titoli."""
    parti = nome_completo.lower().split()
    for parte in parti:
        pulita = parte.rstrip(".")
        if pulita in TITOLI or pulita + "." in TITOLI:
            continue
        if pulita in MASCHILI_IN_A:
            return "m"
        if pulita.endswith("a"):
            return "f"
        return "m"
    return "m"


class Command(BaseCommand):
    help = "Assegna foto profilo ai medici in base al sesso inferito dal nome"

    def add_arguments(self, parser):
        parser.add_argument(
            "--force",
            action="store_true",
            help="Sovrascrive le foto anche per i medici che ne hanno già una",
        )

    def handle(self, *args, **options):
        force = options["force"]
        medici = SchedaMedico.objects.filter(attivo=True).order_by("id")

        if not force:
            medici = medici.filter(foto_url="")

        # Contatori per sesso (per assegnare foto diverse)
        idx = {"f": 0, "m": 0}
        updated = 0

        for medico in medici:
            sesso = _inferisci_sesso(medico.nome_completo)
            pool = FOTO_DONNE if sesso == "f" else FOTO_UOMINI
            foto_url = pool[idx[sesso] % len(pool)]
            idx[sesso] += 1

            medico.foto_url = foto_url
            medico.save(update_fields=["foto_url"])
            genere = "♀" if sesso == "f" else "♂"
            self.stdout.write(f"  {genere} {medico.nome_completo} → {foto_url}")
            updated += 1

        self.stdout.write(self.style.SUCCESS(f"\nAggiornati {updated} medici."))
