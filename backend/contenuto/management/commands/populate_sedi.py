from django.core.management.base import BaseCommand
from prestazioni.models import Struttura


SEDI = [
    {
        "nome": "CDI Milano Centro",
        "cap": "20122",
        "provincia": "MI",
        "lat": 45.4584,
        "lng": 9.2040,
        "foto_url": "https://images.unsplash.com/photo-1587351021759-3e566b6af7cc?w=800&q=80&auto=format&fit=crop",
        "descrizione": (
            "La sede CDI Milano Centro si trova nel cuore di Milano, a pochi passi dalla fermata della "
            "metropolitana Crocetta (linea verde). E' la sede storica del Centro Diagnostico Italiano, "
            "inaugurata nel 1975, dotata di 4 piani di ambulatori e di una delle tecnologie diagnostiche "
            "piu avanzate della Lombardia. Dispone di oltre 80 ambulatori, sale ecografia, diagnostica "
            "per immagini di ultima generazione e un laboratorio analisi con risposta in giornata."
        ),
        "orari": {
            "lun_ven": "07:00 - 20:00",
            "sab": "07:00 - 14:00",
            "dom": "Chiuso",
            "note": "Laboratorio analisi: Lun-Sab dalle 07:00 alle 10:30",
        },
        "servizi": (
            "Cardiologia\nRadiologia e Diagnostica per Immagini\nGinecologia e Ostetricia\n"
            "Neurologia\nOrtopedia e Traumatologia\nDermatologia\nEndocrinologia\n"
            "Gastroenterologia\nOculistica\nOtorinolaringoiatria\nPsichiatria\n"
            "Laboratorio Analisi\nEcografia\nRisonanza Magnetica (3T)\nTC Multistrato\n"
            "Chirurgia in Day Surgery\nCentro Cefalee\nCentro Mappatura Neo"
        ),
    },
    {
        "nome": "CDI Milano Bicocca",
        "cap": "20126",
        "provincia": "MI",
        "lat": 45.5147,
        "lng": 9.2193,
        "foto_url": "https://images.unsplash.com/photo-1586773860418-d37222d8fce3?w=800&q=80&auto=format&fit=crop",
        "descrizione": (
            "Il CDI Milano Bicocca si trova nel quartiere universitario di Sesto San Giovanni/Bicocca, "
            "a due passi dal campus universitario e da uno dei principali hub commerciali e residenziali "
            "del nord Milano. La struttura e moderna e accessibile, con parcheggio convenzionato nelle "
            "vicinanze. Eroga prestazioni specialistiche, ecografiche e laboratoristiche con tempi di "
            "attesa contenuti e orari flessibili."
        ),
        "orari": {
            "lun_ven": "07:30 - 19:30",
            "sab": "07:30 - 13:00",
            "dom": "Chiuso",
            "note": "Prenotazioni telefoniche: 02 00 60 1",
        },
        "servizi": (
            "Cardiologia\nGinecologia\nNeurologia\nOrtopedia\nDermatologia\n"
            "Ecografia\nRadiologia\nLaboratorio Analisi\nFisioterapia\nPediatria"
        ),
    },
    {
        "nome": "CDI Milano Loreto",
        "cap": "20131",
        "provincia": "MI",
        "lat": 45.4844,
        "lng": 9.2243,
        "foto_url": "https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?w=800&q=80&auto=format&fit=crop",
        "descrizione": (
            "Il CDI Milano Loreto e situato nell'area di Piazzale Loreto, uno dei nodi di trasporto piu "
            "importanti di Milano, servito da metro M1 e M2, numerose linee di tram e autobus. "
            "La sede e particolarmente accessibile dai quartieri nord-est della citta. Offre un'ampia "
            "gamma di visite specialistiche, diagnostica per immagini e un efficiente servizio di "
            "prelievi con accettazione senza appuntamento nella fascia mattutina."
        ),
        "orari": {
            "lun_ven": "07:00 - 20:00",
            "sab": "07:00 - 14:00",
            "dom": "Chiuso",
        },
        "servizi": (
            "Cardiologia\nGinecologia\nOrtopedia\nDermatologia\nUrologia\n"
            "Ecografia\nRadiologia\nTC\nLaboratorio Analisi\nFisioterapia\nOculistica"
        ),
    },
    {
        "nome": "CDI Monza",
        "cap": "20900",
        "provincia": "MB",
        "lat": 45.5845,
        "lng": 9.2744,
        "foto_url": "https://images.unsplash.com/photo-1504813184591-01572f98c85f?w=800&q=80&auto=format&fit=crop",
        "descrizione": (
            "Il CDI Monza e il punto di riferimento per la diagnostica medica avanzata in Brianza. "
            "Situato in posizione centrale rispetto al capoluogo brianzolo, la sede e facilmente "
            "raggiungibile in auto e con i mezzi pubblici (autobus da Monza Centrale). "
            "Dispone di ambulatori specialistici, diagnostica per immagini e laboratorio analisi. "
            "Collabora attivamente con gli ospedali del territorio per percorsi di secondo livello."
        ),
        "orari": {
            "lun_ven": "07:30 - 19:30",
            "sab": "07:30 - 13:00",
            "dom": "Chiuso",
        },
        "servizi": (
            "Cardiologia\nNeurologia\nGinecologia\nOrtopedia\nDermatologia\n"
            "Ecografia\nRisonanza Magnetica\nLaboratorio Analisi\nPediatria\nEndocrinologia"
        ),
    },
    {
        "nome": "CDI Bergamo",
        "cap": "24125",
        "provincia": "BG",
        "lat": 45.6939,
        "lng": 9.6817,
        "foto_url": "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=800&q=80&auto=format&fit=crop",
        "descrizione": (
            "Il CDI Bergamo si trova nel quartiere Borgo Palazzo, facilmente raggiungibile dal centro "
            "citta e dalle principali arterie viarie. La struttura offre un servizio completo di "
            "diagnostica ambulatoriale per i residenti di Bergamo e della Valle Seriana. "
            "Dispone di parcheggio privato riservato ai pazienti. La sede e stata recentemente "
            "rinnovata con l'installazione di nuove tecnologie di diagnostica per immagini."
        ),
        "orari": {
            "lun_ven": "07:30 - 19:00",
            "sab": "07:30 - 13:00",
            "dom": "Chiuso",
        },
        "servizi": (
            "Cardiologia\nGinecologia\nOrtopedia\nDermatologia\nNeurologia\n"
            "Ecografia\nRadiologia\nTC\nLaboratorio Analisi\nFisioterapia"
        ),
    },
    {
        "nome": "CDI Brescia",
        "cap": "25124",
        "provincia": "BS",
        "lat": 45.5416,
        "lng": 10.2118,
        "foto_url": "https://images.unsplash.com/photo-1551601651-2a8555f1a136?w=800&q=80&auto=format&fit=crop",
        "descrizione": (
            "Il CDI Brescia e situato nel quartiere Mompiano, nella zona residenziale a nord della citta. "
            "Raggiunte facilmente dalla tangenziale e dal servizio bus urbano, la sede di Brescia offre "
            "prestazioni specialistiche di alta qualita per i residenti della provincia. "
            "E' dotata di un moderno laboratorio analisi, di sale ecografiche e di ambulatori "
            "multidisciplinari. Parcheggio gratuito disponibile per i pazienti."
        ),
        "orari": {
            "lun_ven": "07:30 - 19:00",
            "sab": "07:30 - 13:00",
            "dom": "Chiuso",
        },
        "servizi": (
            "Cardiologia\nGinecologia\nOrtopedia\nDermatologia\nUrologia\n"
            "Ecografia\nRadiologia\nLaboratorio Analisi\nFisioterapia\nPediatria"
        ),
    },
]


class Command(BaseCommand):
    help = "Popola i dati geografici e di dettaglio delle sedi CDI"

    def handle(self, *args, **kwargs):
        for data in SEDI:
            nome = data.pop("nome")
            updated = Struttura.objects.filter(nome=nome).update(**data)
            if updated:
                self.stdout.write(f"  ~ aggiornata: {nome}")
            else:
                self.stdout.write(self.style.WARNING(f"  ! non trovata: {nome}"))

        self.stdout.write(self.style.SUCCESS("\nSedi aggiornate!"))
