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

# fit=facearea&facepad=3 → Unsplash face-detection crop (ritaglia sul viso)
_FP = "?w=400&h=400&q=80&auto=format&fit=facearea&facepad=3"

FOTO_DONNE = [
    f"https://images.unsplash.com/photo-1559839734-2b71ea197ec2{_FP}",   # camice bianco, capelli corti
    f"https://images.unsplash.com/photo-1594824476967-48c8b964273f{_FP}", # stetoscopio, sorridente
    f"https://images.unsplash.com/photo-1614608682850-e0d6ed316d47{_FP}", # camice bianco, capelli scuri
    f"https://images.unsplash.com/photo-1527613426441-4da17471b66d{_FP}", # laboratorio, tratti europei
    f"https://images.unsplash.com/photo-1623854767648-e7bb8009f0db{_FP}", # camice bianco, sorriso
    f"https://images.unsplash.com/photo-1551601651-2a8555f1a136{_FP}",   # medico femminile
    f"https://images.unsplash.com/photo-1573496359142-b8d87734a5a2{_FP}", # professionista sanitaria
    f"https://images.unsplash.com/photo-1607746882042-944635dfe10e{_FP}", # ritratto medico
    f"https://images.unsplash.com/photo-1581091226825-a6a2a5aee158{_FP}", # dottoressa sorridente
    f"https://images.unsplash.com/photo-1530026405186-ed1f139313f8{_FP}", # medico, volto frontale
]

FOTO_UOMINI = [
    f"https://images.unsplash.com/photo-1612349317150-e413f6a5b16d{_FP}", # camice, barba scura, mediterraneo
    f"https://images.unsplash.com/photo-1582750433449-648ed127bb54{_FP}", # camice, mascherina
    f"https://images.unsplash.com/photo-1618498082410-b4aa22193b38{_FP}", # chirurgo, occhi chiari
    f"https://images.unsplash.com/photo-1537368910025-700350fe46c7{_FP}", # dottore stetoscopio
    f"https://images.unsplash.com/photo-1622253692010-333f2da6031d{_FP}", # medico maschio
    f"https://images.unsplash.com/photo-1560250097-0b93528c311a{_FP}",   # professionista camice
    f"https://images.unsplash.com/photo-1585842378054-ee2e52f94ba2{_FP}", # dottore ritratto
    f"https://images.unsplash.com/photo-1496247749665-49cf5b1022e9{_FP}", # medico anziano
    f"https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d{_FP}", # professionista maschile
    f"https://images.unsplash.com/photo-1472099645785-5658abf4ff4e{_FP}", # ritratto uomo professionale
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
