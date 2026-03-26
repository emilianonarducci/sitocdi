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

# Pool di ritratti medici con camice bianco — Unsplash (verificati HTTP 200)
FOTO_DONNE = [
    "https://images.unsplash.com/photo-1719461341347-dac3e2087b59?w=400&q=80&auto=format&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1759350075317-0ef24bee0428?w=400&q=80&auto=format&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1676552055618-22ec8cde399a?w=400&q=80&auto=format&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1753486986927-ff09dafb99a1?w=400&q=80&auto=format&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1759350075177-eeb89d507990?w=400&q=80&auto=format&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1753487050317-919a2b26a6ed?w=400&q=80&auto=format&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1759350075145-92fa877c632a?w=400&q=80&auto=format&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1754715203698-70c7ad3a879d?w=400&q=80&auto=format&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1601852645220-cdb448d013ff?w=400&q=80&auto=format&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1698779745239-aef2a07781e5?w=400&q=80&auto=format&fit=crop&crop=face",
]

FOTO_UOMINI = [
    "https://images.unsplash.com/photo-1645066928295-2506defde470?w=400&q=80&auto=format&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1642975967602-653d378f3b5b?w=400&q=80&auto=format&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1655559704433-36945d173a47?w=400&q=80&auto=format&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1751006846381-6c379742b08a?w=400&q=80&auto=format&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1741336649522-f0652dfdab1b?w=400&q=80&auto=format&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1748288166888-f1bd5d6ef9ed?w=400&q=80&auto=format&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1638109879065-10b4a3bf0360?w=400&q=80&auto=format&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1712687947291-8e89f1f426ab?w=400&q=80&auto=format&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1745758278377-2b42af378614?w=400&q=80&auto=format&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1681235853990-5c343a759dca?w=400&q=80&auto=format&fit=crop&crop=face",
]

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
