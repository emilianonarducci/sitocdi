from django.core.management.base import BaseCommand
from prestazioni.models import Fondo, Struttura, Medico, Prestazione
from prestazioni.search import create_index, index_prestazione


class Command(BaseCommand):
    help = "Popola il database con dati di esempio CDI"

    def handle(self, *args, **kwargs):
        self.stdout.write("Creazione fondi...")
        fondi = {
            "FASI": Fondo.objects.get_or_create(nome="FASI", codice="FASI")[0],
            "Metasalute": Fondo.objects.get_or_create(nome="Metasalute", codice="META")[0],
            "FASDAC": Fondo.objects.get_or_create(nome="FASDAC", codice="FASDAC")[0],
            "Previmedical": Fondo.objects.get_or_create(nome="Previmedical", codice="PREV")[0],
            "Unisalute": Fondo.objects.get_or_create(nome="Unisalute", codice="UNIS")[0],
        }

        self.stdout.write("Creazione strutture CDI...")
        strutture = {
            "Milano Centro": Struttura.objects.get_or_create(
                nome="CDI Milano Centro", defaults={"tipo": "poliambulatorio", "citta": "Milano", "indirizzo": "Via San Barnaba, 29"}
            )[0],
            "Milano Bicocca": Struttura.objects.get_or_create(
                nome="CDI Milano Bicocca", defaults={"tipo": "poliambulatorio", "citta": "Milano", "indirizzo": "Via Libero Temolo, 4"}
            )[0],
            "Monza": Struttura.objects.get_or_create(
                nome="CDI Monza", defaults={"tipo": "poliambulatorio", "citta": "Monza", "indirizzo": "Via Solferino, 16"}
            )[0],
            "Bergamo": Struttura.objects.get_or_create(
                nome="CDI Bergamo", defaults={"tipo": "poliambulatorio", "citta": "Bergamo", "indirizzo": "Via Borgo Palazzo, 130"}
            )[0],
            "Brescia": Struttura.objects.get_or_create(
                nome="CDI Brescia", defaults={"tipo": "poliambulatorio", "citta": "Brescia", "indirizzo": "Via Cefalonia, 70"}
            )[0],
            "Milano Loreto": Struttura.objects.get_or_create(
                nome="CDI Milano Loreto", defaults={"tipo": "poliambulatorio", "citta": "Milano", "indirizzo": "Piazzale Loreto, 7"}
            )[0],
        }

        self.stdout.write("Creazione medici...")
        medici = {
            "Rossi": Medico.objects.get_or_create(
                nome="Marco", cognome="Rossi",
                defaults={"specializzazione": "Cardiologia"}
            )[0],
            "Bianchi": Medico.objects.get_or_create(
                nome="Laura", cognome="Bianchi",
                defaults={"specializzazione": "Ginecologia"}
            )[0],
            "Ferrari": Medico.objects.get_or_create(
                nome="Giovanni", cognome="Ferrari",
                defaults={"specializzazione": "Ortopedia"}
            )[0],
            "Conti": Medico.objects.get_or_create(
                nome="Sofia", cognome="Conti",
                defaults={"specializzazione": "Neurologia"}
            )[0],
            "Ricci": Medico.objects.get_or_create(
                nome="Paolo", cognome="Ricci",
                defaults={"specializzazione": "Radiologia"}
            )[0],
            "Marino": Medico.objects.get_or_create(
                nome="Anna", cognome="Marino",
                defaults={"specializzazione": "Dermatologia"}
            )[0],
        }

        # Associa medici alle strutture
        medici["Rossi"].strutture.set([strutture["Milano Centro"], strutture["Monza"]])
        medici["Bianchi"].strutture.set([strutture["Milano Centro"], strutture["Milano Bicocca"]])
        medici["Ferrari"].strutture.set([strutture["Bergamo"], strutture["Brescia"]])
        medici["Conti"].strutture.set([strutture["Milano Centro"], strutture["Milano Loreto"]])
        medici["Ricci"].strutture.set(list(strutture.values()))
        medici["Marino"].strutture.set([strutture["Milano Bicocca"], strutture["Milano Loreto"]])

        self.stdout.write("Creazione prestazioni...")
        prestazioni_data = [
            {
                "nome": "Visita cardiologica",
                "codice": "89.7",
                "branca": "cardiologia",
                "descrizione": "Visita specialistica cardiologica con anamnesi ed esame obiettivo completo.",
                "prezzo_solvente": 150.00,
                "strutture": ["Milano Centro", "Monza", "Bergamo"],
                "medici": ["Rossi"],
                "fondi": ["FASI", "Metasalute", "Unisalute"],
            },
            {
                "nome": "Elettrocardiogramma (ECG)",
                "codice": "89.52",
                "branca": "cardiologia",
                "descrizione": "Registrazione dell'attività elettrica del cuore a riposo.",
                "prezzo_solvente": 45.00,
                "strutture": ["Milano Centro", "Milano Bicocca", "Monza", "Bergamo", "Brescia", "Milano Loreto"],
                "medici": ["Rossi"],
                "fondi": ["FASI", "Metasalute", "FASDAC", "Previmedical", "Unisalute"],
            },
            {
                "nome": "Ecografia addome completo",
                "codice": "88.76",
                "branca": "radiologia",
                "descrizione": "Ecografia dell'addome superiore e inferiore con valutazione degli organi addominali.",
                "prezzo_solvente": 120.00,
                "strutture": ["Milano Centro", "Milano Bicocca", "Monza"],
                "medici": ["Ricci"],
                "fondi": ["Metasalute", "FASDAC"],
            },
            {
                "nome": "Risonanza magnetica colonna lombare",
                "codice": "88.93",
                "branca": "radiologia",
                "descrizione": "RM della colonna lombare con e senza mezzo di contrasto.",
                "prezzo_solvente": 280.00,
                "strutture": ["Milano Centro", "Bergamo"],
                "medici": ["Ricci"],
                "fondi": ["FASI", "Unisalute"],
            },
            {
                "nome": "Visita ginecologica",
                "codice": "89.26",
                "branca": "ginecologia",
                "descrizione": "Visita specialistica ginecologica con esame obiettivo.",
                "prezzo_solvente": 130.00,
                "strutture": ["Milano Centro", "Milano Bicocca", "Milano Loreto"],
                "medici": ["Bianchi"],
                "fondi": ["FASI", "Metasalute", "Previmedical"],
            },
            {
                "nome": "Pap test",
                "codice": "91.46",
                "branca": "ginecologia",
                "descrizione": "Esame citologico del collo dell'utero per screening cervicale.",
                "prezzo_solvente": 55.00,
                "strutture": ["Milano Centro", "Milano Bicocca"],
                "medici": ["Bianchi"],
                "fondi": ["FASI", "Metasalute", "FASDAC", "Unisalute"],
            },
            {
                "nome": "Visita ortopedica",
                "codice": "89.7",
                "branca": "ortopedia",
                "descrizione": "Visita specialistica ortopedica con valutazione dell'apparato muscolo-scheletrico.",
                "prezzo_solvente": 140.00,
                "strutture": ["Bergamo", "Brescia", "Monza"],
                "medici": ["Ferrari"],
                "fondi": ["FASI", "FASDAC", "Previmedical"],
            },
            {
                "nome": "Radiografia colonna cervicale",
                "codice": "87.22",
                "branca": "radiologia",
                "descrizione": "Esame radiografico della colonna cervicale in due proiezioni.",
                "prezzo_solvente": 65.00,
                "strutture": ["Milano Centro", "Milano Bicocca", "Bergamo", "Brescia"],
                "medici": ["Ricci"],
                "fondi": ["Metasalute", "FASDAC", "Previmedical"],
            },
            {
                "nome": "Visita neurologica",
                "codice": "89.13",
                "branca": "neurologia",
                "descrizione": "Visita specialistica neurologica con valutazione del sistema nervoso.",
                "prezzo_solvente": 160.00,
                "strutture": ["Milano Centro", "Milano Loreto"],
                "medici": ["Conti"],
                "fondi": ["FASI", "Unisalute"],
            },
            {
                "nome": "Visita dermatologica",
                "codice": "89.7",
                "branca": "dermatologia",
                "descrizione": "Visita specialistica dermatologica con dermatoscopia dei nei.",
                "prezzo_solvente": 110.00,
                "strutture": ["Milano Bicocca", "Milano Loreto"],
                "medici": ["Marino"],
                "fondi": ["Metasalute", "Previmedical"],
            },
            {
                "nome": "Holter cardiaco 24h",
                "codice": "89.50",
                "branca": "cardiologia",
                "descrizione": "Monitoraggio elettrocardiografico continuo nelle 24 ore.",
                "prezzo_solvente": 95.00,
                "strutture": ["Milano Centro", "Monza"],
                "medici": ["Rossi"],
                "fondi": ["FASI", "Metasalute", "FASDAC"],
            },
            {
                "nome": "Esame del sangue completo",
                "codice": "90.62",
                "branca": "laboratorio",
                "descrizione": "Emocromo completo con formula leucocitaria, glicemia, colesterolo, trigliceridi.",
                "prezzo_solvente": 40.00,
                "strutture": ["Milano Centro", "Milano Bicocca", "Monza", "Bergamo", "Brescia", "Milano Loreto"],
                "medici": [],
                "fondi": ["FASI", "Metasalute", "FASDAC", "Previmedical", "Unisalute"],
            },
            {
                "nome": "TAC torace",
                "codice": "87.41",
                "branca": "radiologia",
                "descrizione": "Tomografia assiale computerizzata del torace senza e con mezzo di contrasto.",
                "prezzo_solvente": 240.00,
                "strutture": ["Milano Centro", "Bergamo"],
                "medici": ["Ricci"],
                "fondi": ["FASI", "Unisalute"],
            },
            {
                "nome": "Fisioterapia seduta",
                "codice": "93.14",
                "branca": "fisioterapia",
                "descrizione": "Seduta di fisioterapia individuale con terapista specializzato.",
                "prezzo_solvente": 60.00,
                "strutture": ["Brescia", "Bergamo", "Monza"],
                "medici": [],
                "fondi": ["Metasalute", "FASDAC", "Previmedical"],
            },
            {
                "nome": "Ecografia tiroide",
                "codice": "88.71",
                "branca": "radiologia",
                "descrizione": "Ecografia della ghiandola tiroidea con valutazione di noduli.",
                "prezzo_solvente": 90.00,
                "strutture": ["Milano Centro", "Milano Bicocca", "Monza"],
                "medici": ["Ricci"],
                "fondi": ["FASI", "Metasalute", "Previmedical"],
            },
        ]

        # Tenta di creare l'indice OpenSearch (ignorato se non disponibile)
        try:
            create_index()
        except Exception:
            self.stdout.write("  ⚠ OpenSearch non disponibile, uso solo PostgreSQL")

        for data in prestazioni_data:
            p, created = Prestazione.objects.get_or_create(
                nome=data["nome"],
                defaults={
                    "codice": data["codice"],
                    "branca": data["branca"],
                    "descrizione": data["descrizione"],
                    "prezzo_solvente": data["prezzo_solvente"],
                    "attiva": True,
                },
            )
            if created:
                p.strutture.set([strutture[s] for s in data["strutture"]])
                p.medici.set([medici[m] for m in data["medici"]])
                p.fondi.set([fondi[f] for f in data["fondi"]])
                try:
                    index_prestazione(p)
                except Exception:
                    pass
                self.stdout.write(f"  ✓ {p.nome}")
            else:
                self.stdout.write(f"  — già esistente: {p.nome}")

        self.stdout.write(self.style.SUCCESS(
            f"\nFatto! {len(prestazioni_data)} prestazioni, {len(strutture)} strutture, {len(fondi)} fondi."
        ))
