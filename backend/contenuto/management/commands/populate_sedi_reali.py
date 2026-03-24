"""
Popola le sedi CDI reali da https://www.cdi.it/il-centro-diagnostico-italiano/le-nostre-sedi/
"""
from django.core.management.base import BaseCommand
from prestazioni.models import Struttura

# Foto riutilizzate per categoria
FOTO_POLI = "https://images.unsplash.com/photo-1587351021759-3e566b6af7cc?w=800&q=80&auto=format&fit=crop"
FOTO_LAB  = "https://images.unsplash.com/photo-1532187863486-abf9dbad1b69?w=800&q=80&auto=format&fit=crop"
FOTO_FKT  = "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=800&q=80&auto=format&fit=crop"
FOTO_DEN  = "https://images.unsplash.com/photo-1588776814546-ec7e4b5c7c58?w=800&q=80&auto=format&fit=crop"
FOTO_EXT  = "https://images.unsplash.com/photo-1504813184591-01572f98c85f?w=800&q=80&auto=format&fit=crop"

ORARI_STD = {"lun_ven": "07:00 - 20:00", "sab": "07:00 - 14:00", "dom": "Chiuso"}
ORARI_PRE = {"lun_ven": "07:00 - 11:00", "sab": "07:00 - 10:30", "dom": "Chiuso", "note": "Solo prelievi, senza appuntamento in fascia mattutina"}
ORARI_EXT = {"lun_ven": "07:30 - 19:00", "sab": "07:30 - 13:00", "dom": "Chiuso"}

SERV_POLI = (
    "Cardiologia\nRadiologia e Diagnostica per Immagini\nGinecologia e Ostetricia\n"
    "Neurologia\nOrtopedia e Traumatologia\nDermatologia\nEndocrinologia\n"
    "Gastroenterologia\nOculistica\nOtorinolaringoiatria\nLaboratorio Analisi\n"
    "Ecografia\nRisonanza Magnetica\nTC Multistrato"
)
SERV_PRE = "Prelievi ematici\nEsami delle urine\nEsami colturali\nPrelievi a domicilio su richiesta"
SERV_FKT = "Fisioterapia\nRiabilitazione ortopedica\nLinfodrenaggio\nTecarterapia\nLaserterapia\nChinesiterapia"
SERV_DEN = "Odontoiatria\nOrtognatodonzia\nImplantologia\nIgiene dentale\nChirurgia orale\nEstetica dentale"
SERV_SME = (
    "Cardiologia\nDermatologia\nGinecologia\nNeurologia\nOrtopedia\n"
    "Oculistica\nOtorinolaringoiatria\nLaboratorio Analisi\nEcografia"
)

SEDI = [
    # ─── MILANO CITTÀ ────────────────────────────────────────────────────────
    {
        "nome": "CDI Saint Bon",
        "tipo": "poliambulatorio",
        "indirizzo": "Via Saint Bon, 20",
        "cap": "20147",
        "citta": "Milano",
        "provincia": "MI",
        "telefono": "02 48317444",
        "lat": 45.4635, "lng": 9.1534,
        "foto_url": FOTO_POLI,
        "descrizione": (
            "La sede CDI Saint Bon e il cuore operativo del Centro Diagnostico Italiano, "
            "situata nel quartiere Lorenteggio. Offre l'intera gamma di specialita mediche, "
            "dalla diagnostica per immagini alle visite specialistiche, con un laboratorio analisi "
            "di primo livello e tecnologie di ultima generazione."
        ),
        "orari": ORARI_STD,
        "servizi": SERV_POLI,
    },
    {
        "nome": "CDI Fisioterapia e Riabilitazione Saint Bon",
        "tipo": "poliambulatorio",
        "indirizzo": "Via Saint Bon, 36",
        "cap": "20147",
        "citta": "Milano",
        "provincia": "MI",
        "telefono": "02 48317386",
        "lat": 45.4633, "lng": 9.1531,
        "foto_url": FOTO_FKT,
        "descrizione": (
            "Centro dedicato alla fisioterapia e riabilitazione, adiacente alla sede principale di Via Saint Bon. "
            "Dispone di palestre attrezzate, cabine per trattamenti individuali e strumentazione "
            "per terapia fisica avanzata."
        ),
        "orari": ORARI_STD,
        "servizi": SERV_FKT,
    },
    {
        "nome": "CDI Dental & Face",
        "tipo": "studio",
        "indirizzo": "Via Saint Bon, 16",
        "cap": "20147",
        "citta": "Milano",
        "provincia": "MI",
        "telefono": "02 48317425",
        "lat": 45.4637, "lng": 9.1536,
        "foto_url": FOTO_DEN,
        "descrizione": (
            "Studio odontoiatrico CDI Dental & Face, specializzato in odontoiatria estetica, "
            "implantologia e ortodonzia. Utilizza tecnologie digitali di ultima generazione "
            "per diagnosi e trattamenti di precisione."
        ),
        "orari": ORARI_STD,
        "servizi": SERV_DEN,
    },
    {
        "nome": "Bionics Cairoli",
        "tipo": "poliambulatorio",
        "indirizzo": "Largo Cairoli, 2",
        "cap": "20121",
        "citta": "Milano",
        "provincia": "MI",
        "telefono": "02 48317444",
        "lat": 45.4668, "lng": 9.1822,
        "foto_url": FOTO_POLI,
        "descrizione": (
            "Poliambulatorio Bionics in pieno centro di Milano, a due passi dal Castello Sforzesco "
            "e dalla fermata metro Cairoli. Accesso facilitato dalla linea M1. "
            "Offre visite specialistiche, diagnostica strumentale e laboratorio analisi."
        ),
        "orari": ORARI_STD,
        "servizi": SERV_POLI,
    },
    {
        "nome": "Bionics Portello",
        "tipo": "poliambulatorio",
        "indirizzo": "Via Grosotto, 7",
        "cap": "20149",
        "citta": "Milano",
        "provincia": "MI",
        "telefono": "02 48317444",
        "lat": 45.4810, "lng": 9.1487,
        "foto_url": FOTO_POLI,
        "descrizione": (
            "Il Bionics Portello si trova nell'omonimo quartiere in rapida crescita, "
            "vicino al centro commerciale Portello e alla fermata metro Lotto. "
            "Struttura moderna con diagnostica per immagini, laboratorio e ambulatori specialistici."
        ),
        "orari": ORARI_STD,
        "servizi": SERV_POLI,
    },
    {
        "nome": "Portello Punto Prelievi",
        "tipo": "altro",
        "indirizzo": "Via Grosotto, 7",
        "cap": "20149",
        "citta": "Milano",
        "provincia": "MI",
        "telefono": "02 48317555",
        "lat": 45.4811, "lng": 9.1488,
        "foto_url": FOTO_LAB,
        "descrizione": "Punto prelievi SSN integrato nel complesso Bionics Portello. Accettazione senza appuntamento nelle ore mattutine.",
        "orari": ORARI_PRE,
        "servizi": SERV_PRE,
    },
    {
        "nome": "Bionics Porta Nuova",
        "tipo": "poliambulatorio",
        "indirizzo": "Piazza Gae Aulenti, 4",
        "cap": "20124",
        "citta": "Milano",
        "provincia": "MI",
        "telefono": "02 48317444",
        "lat": 45.4842, "lng": 9.1903,
        "foto_url": FOTO_POLI,
        "descrizione": (
            "Poliambulatorio Bionics nel cuore del distretto Porta Nuova, uno dei quartieri "
            "piu moderni di Milano. Facilmente raggiungibile con metro M2 (Gioia) e M5 (Isola). "
            "Servizi specialistici di alto livello in un contesto architettonico contemporaneo."
        ),
        "orari": ORARI_STD,
        "servizi": SERV_POLI,
    },
    {
        "nome": "Bionics Largo Augusto",
        "tipo": "poliambulatorio",
        "indirizzo": "Corso Porta Vittoria, 5",
        "cap": "20122",
        "citta": "Milano",
        "provincia": "MI",
        "telefono": "02 48317444",
        "lat": 45.4615, "lng": 9.2007,
        "foto_url": FOTO_POLI,
        "descrizione": (
            "Centro medico nel cuore di Milano, vicinissimo al Duomo e alla fermata metro San Babila. "
            "Ideale per chi lavora in centro citta. Ambulatori di cardiologia, neurologia, ortopedia "
            "e diagnostica strumentale con orari flessibili."
        ),
        "orari": ORARI_STD,
        "servizi": SERV_POLI,
    },
    {
        "nome": "Bionics Lavater (Porta Venezia)",
        "tipo": "poliambulatorio",
        "indirizzo": "Via Omboni, 8",
        "cap": "20129",
        "citta": "Milano",
        "provincia": "MI",
        "telefono": "02 48317444",
        "lat": 45.4721, "lng": 9.2096,
        "foto_url": FOTO_POLI,
        "descrizione": (
            "Poliambulatorio Bionics nel quartiere Porta Venezia, uno dei piu vivaci di Milano. "
            "Metro Lima (M1) a 5 minuti a piedi. Offre un'ampia gamma di specialita mediche "
            "con personale altamente qualificato."
        ),
        "orari": ORARI_STD,
        "servizi": SERV_POLI,
    },
    {
        "nome": "CDI Viale Monza",
        "tipo": "poliambulatorio",
        "indirizzo": "Viale Monza, 270",
        "cap": "20126",
        "citta": "Milano",
        "provincia": "MI",
        "telefono": "02 48317555",
        "lat": 45.5023, "lng": 9.2326,
        "foto_url": FOTO_POLI,
        "descrizione": (
            "Sede CDI in Viale Monza, nel nord-est di Milano. "
            "Laboratorio analisi, diagnostica per immagini e visite specialistiche. "
            "Ampio parcheggio nelle vicinanze."
        ),
        "orari": ORARI_STD,
        "servizi": SERV_POLI,
    },
    {
        "nome": "Bionics Viale Monza",
        "tipo": "poliambulatorio",
        "indirizzo": "Viale Monza, 270 (4° piano)",
        "cap": "20126",
        "citta": "Milano",
        "provincia": "MI",
        "telefono": "02 48317444",
        "lat": 45.5024, "lng": 9.2327,
        "foto_url": FOTO_POLI,
        "descrizione": "Poliambulatorio Bionics al quarto piano del complesso di Viale Monza 270, con specialita complementari al CDI del piano inferiore.",
        "orari": ORARI_STD,
        "servizi": SERV_POLI,
    },
    {
        "nome": "Bionics Navigli",
        "tipo": "poliambulatorio",
        "indirizzo": "Viale Liguria, 23",
        "cap": "20143",
        "citta": "Milano",
        "provincia": "MI",
        "telefono": "02 48317444",
        "lat": 45.4480, "lng": 9.1828,
        "foto_url": FOTO_POLI,
        "descrizione": (
            "Poliambulatorio Bionics nel quartiere Navigli, raggiungibile con la metro M2 (Romolo) "
            "o con diverse linee di tram. Visite specialistiche, fisioterapia, odontoiatria "
            "e laboratorio analisi in un'unica struttura."
        ),
        "orari": ORARI_STD,
        "servizi": SERV_POLI,
    },
    {
        "nome": "Navigli Punto Prelievi SSN",
        "tipo": "altro",
        "indirizzo": "Viale Liguria, 23",
        "cap": "20143",
        "citta": "Milano",
        "provincia": "MI",
        "telefono": "02 48317555",
        "lat": 45.4479, "lng": 9.1827,
        "foto_url": FOTO_LAB,
        "descrizione": "Punto prelievi SSN presso il complesso Bionics Navigli. Accesso diretto, senza appuntamento nelle prime ore del mattino.",
        "orari": ORARI_PRE,
        "servizi": SERV_PRE,
    },
    {
        "nome": "Bionics Citylife",
        "tipo": "poliambulatorio",
        "indirizzo": "Piazza Tre Torri",
        "cap": "20145",
        "citta": "Milano",
        "provincia": "MI",
        "telefono": "02 48317444",
        "lat": 45.4780, "lng": 9.1358,
        "foto_url": FOTO_POLI,
        "descrizione": (
            "Poliambulatorio Bionics nel distretto Citylife, uno dei complessi urbani piu moderni "
            "d'Europa. Accesso con metro M5 (Tre Torri). Struttura all'avanguardia con tecnologie "
            "diagnostiche di ultima generazione, parcheggio nel complesso."
        ),
        "orari": ORARI_STD,
        "servizi": SERV_POLI,
    },
    {
        "nome": "Citylife Punto Prelievi SSN",
        "tipo": "altro",
        "indirizzo": "Piazza Tre Torri",
        "cap": "20145",
        "citta": "Milano",
        "provincia": "MI",
        "telefono": "02 48317555",
        "lat": 45.4781, "lng": 9.1359,
        "foto_url": FOTO_LAB,
        "descrizione": "Punto prelievi SSN integrato nel complesso Bionics Citylife. Accesso dal piano terra, senza appuntamento.",
        "orari": ORARI_PRE,
        "servizi": SERV_PRE,
    },
    {
        "nome": "Bionics Bicocca",
        "tipo": "poliambulatorio",
        "indirizzo": "Via Temolo, 3",
        "cap": "20126",
        "citta": "Milano",
        "provincia": "MI",
        "telefono": "02 48317444",
        "lat": 45.5147, "lng": 9.2193,
        "foto_url": FOTO_POLI,
        "descrizione": (
            "Poliambulatorio Bionics nel quartiere Bicocca, accanto al campus universitario. "
            "Metro M5 (Bicocca) a pochi minuti. Visite specialistiche, diagnostica strumentale "
            "e laboratorio con risposte rapide."
        ),
        "orari": ORARI_STD,
        "servizi": SERV_POLI,
    },
    {
        "nome": "Bicocca Punto Prelievi SSN",
        "tipo": "altro",
        "indirizzo": "Via Temolo, 3",
        "cap": "20126",
        "citta": "Milano",
        "provincia": "MI",
        "telefono": "02 48317555",
        "lat": 45.5148, "lng": 9.2192,
        "foto_url": FOTO_LAB,
        "descrizione": "Punto prelievi SSN presso il complesso Bionics Bicocca.",
        "orari": ORARI_PRE,
        "servizi": SERV_PRE,
    },
    {
        "nome": "CDI Pellegrino Rossi",
        "tipo": "poliambulatorio",
        "indirizzo": "Via Pellegrino Rossi, 24",
        "cap": "20161",
        "citta": "Milano",
        "provincia": "MI",
        "telefono": "02 48317555",
        "lat": 45.5134, "lng": 9.1698,
        "foto_url": FOTO_POLI,
        "descrizione": (
            "Sede CDI nel quartiere Niguarda, vicino all'omonimo Ospedale. "
            "Poliambulatorio con laboratorio analisi, ecografia, radiologia e specialita mediche. "
            "Servito da diverse linee di autobus del nord di Milano."
        ),
        "orari": ORARI_STD,
        "servizi": SERV_POLI,
    },
    {
        "nome": "Bionics Symbiosis",
        "tipo": "poliambulatorio",
        "indirizzo": "Via Vezza d'Oglio, 3-7",
        "cap": "20141",
        "citta": "Milano",
        "provincia": "MI",
        "telefono": "02 48317444",
        "lat": 45.4400, "lng": 9.1900,
        "foto_url": FOTO_POLI,
        "descrizione": (
            "Poliambulatorio Bionics nel complesso residenziale Symbiosis, nel sud di Milano. "
            "Struttura moderna con servizi medici integrati, diagnostica per immagini e laboratorio. "
            "Facilmente raggiungibile con il tram da Porta Romana."
        ),
        "orari": ORARI_STD,
        "servizi": SERV_POLI,
    },
    {
        "nome": "Symbiosis Punto Prelievi SSN",
        "tipo": "altro",
        "indirizzo": "Via Vezza d'Oglio, 3-7",
        "cap": "20141",
        "citta": "Milano",
        "provincia": "MI",
        "telefono": "800 638638",
        "lat": 45.4401, "lng": 9.1901,
        "foto_url": FOTO_LAB,
        "descrizione": "Punto prelievi SSN nel complesso Symbiosis. Numero verde gratuito per prenotazioni.",
        "orari": ORARI_PRE,
        "servizi": SERV_PRE,
    },
    {
        "nome": "Corso Italia Punto Prelievi SSN",
        "tipo": "altro",
        "indirizzo": "Corso Italia, 46",
        "cap": "20122",
        "citta": "Milano",
        "provincia": "MI",
        "telefono": "02 48317555",
        "lat": 45.4563, "lng": 9.1852,
        "foto_url": FOTO_LAB,
        "descrizione": "Punto prelievi SSN in posizione centrale, su Corso Italia, a pochi passi dal Duomo.",
        "orari": ORARI_PRE,
        "servizi": SERV_PRE,
    },
    {
        "nome": "Abruzzi Punto Prelievi SSN",
        "tipo": "altro",
        "indirizzo": "Viale Abruzzi, 56",
        "cap": "20131",
        "citta": "Milano",
        "provincia": "MI",
        "telefono": "02 48317555",
        "lat": 45.4820, "lng": 9.2216,
        "foto_url": FOTO_LAB,
        "descrizione": "Punto prelievi SSN in Viale Abruzzi, zona Loreto/Buenos Aires. Metro M1/M2 Loreto a 5 minuti.",
        "orari": ORARI_PRE,
        "servizi": SERV_PRE,
    },
    {
        "nome": "Giulio Romano Punto Prelievi SSN",
        "tipo": "altro",
        "indirizzo": "Via Giulio Romano, 17",
        "cap": "20135",
        "citta": "Milano",
        "provincia": "MI",
        "telefono": "02 48317555",
        "lat": 45.4483, "lng": 9.2083,
        "foto_url": FOTO_LAB,
        "descrizione": "Punto prelievi SSN nella zona Porta Romana / Crocetta. Metro M3 Crocetta raggiungibile a piedi.",
        "orari": ORARI_PRE,
        "servizi": SERV_PRE,
    },
    # ─── PROVINCIA DI MILANO ─────────────────────────────────────────────────
    {
        "nome": "CDI Cernusco sul Naviglio",
        "tipo": "poliambulatorio",
        "indirizzo": "Via Torino, 8",
        "cap": "20063",
        "citta": "Cernusco sul Naviglio",
        "provincia": "MI",
        "telefono": "02 48317555",
        "lat": 45.5225, "lng": 9.3309,
        "foto_url": FOTO_EXT,
        "descrizione": (
            "Poliambulatorio CDI a Cernusco sul Naviglio, facilmente raggiungibile dalla Metro M2 "
            "(Cernusco) e dalla tangenziale est. Serve i comuni dell'est milanese con visite "
            "specialistiche, ecografie e laboratorio analisi."
        ),
        "orari": ORARI_EXT,
        "servizi": SERV_SME,
    },
    {
        "nome": "CDI Corsico",
        "tipo": "poliambulatorio",
        "indirizzo": "Via Vecchia Vigevanese, 4",
        "cap": "20094",
        "citta": "Corsico",
        "provincia": "MI",
        "telefono": "02 48317555",
        "lat": 45.4338, "lng": 9.1140,
        "foto_url": FOTO_EXT,
        "descrizione": (
            "Poliambulatorio CDI a Corsico, nel sud-ovest dell'hinterland milanese. "
            "Raggiungibile dalla tangenziale ovest (uscita Corsico). Parcheggio disponibile. "
            "Offre prestazioni specialistiche per i residenti dei comuni del Naviglio Grande."
        ),
        "orari": ORARI_EXT,
        "servizi": SERV_SME,
    },
    {
        "nome": "CDI Legnano",
        "tipo": "poliambulatorio",
        "indirizzo": "Corso Italia, 32",
        "cap": "20025",
        "citta": "Legnano",
        "provincia": "MI",
        "telefono": "02 48317555",
        "lat": 45.5950, "lng": 8.9181,
        "foto_url": FOTO_EXT,
        "descrizione": (
            "Poliambulatorio CDI in centro a Legnano, capoluogo dell'Alto Milanese. "
            "Raggiungibile con il treno (stazione Legnano) e la tangenziale ovest. "
            "Offre le principali specialita mediche per i residenti della zona."
        ),
        "orari": ORARI_EXT,
        "servizi": SERV_SME,
    },
    {
        "nome": "CDI Rho",
        "tipo": "poliambulatorio",
        "indirizzo": "Via Magenta, 41",
        "cap": "20017",
        "citta": "Rho",
        "provincia": "MI",
        "telefono": "02 48317555",
        "lat": 45.5300, "lng": 9.0395,
        "foto_url": FOTO_EXT,
        "descrizione": (
            "Poliambulatorio CDI a Rho, a pochi minuti dalla Fiera di Milano e dall'aeroporto di Malpensa. "
            "Servito dalla metro M1 (Rho Fiera). Specialita mediche, diagnostica e laboratorio analisi."
        ),
        "orari": ORARI_EXT,
        "servizi": SERV_SME,
    },
    # ─── PAVIA ───────────────────────────────────────────────────────────────
    {
        "nome": "CDI Pavia",
        "tipo": "poliambulatorio",
        "indirizzo": "Viale della Liberta, 83",
        "cap": "27100",
        "citta": "Pavia",
        "provincia": "PV",
        "telefono": "02 78637131",
        "lat": 45.1847, "lng": 9.1582,
        "foto_url": FOTO_EXT,
        "descrizione": (
            "Poliambulatorio CDI a Pavia, sul viale principale della citta universitaria. "
            "Punto di riferimento per la diagnostica avanzata nel pavese. "
            "Collegato con Milano via treno (30 minuti dalla Stazione Centrale)."
        ),
        "orari": ORARI_EXT,
        "servizi": SERV_SME,
    },
    # ─── VARESE ──────────────────────────────────────────────────────────────
    {
        "nome": "CDI Varese",
        "tipo": "poliambulatorio",
        "indirizzo": "Via Sacco, 8",
        "cap": "21100",
        "citta": "Varese",
        "provincia": "VA",
        "telefono": "02 48317555",
        "lat": 45.8204, "lng": 8.8257,
        "foto_url": FOTO_EXT,
        "descrizione": (
            "Poliambulatorio CDI in centro a Varese, capoluogo dell'omonima provincia. "
            "Facilmente raggiungibile dal centro citta e dalla stazione FS. "
            "Offre le principali specialita mediche e diagnostica strumentale."
        ),
        "orari": ORARI_EXT,
        "servizi": SERV_SME,
    },
    {
        "nome": "Centro Medico SME Varese",
        "tipo": "poliambulatorio",
        "indirizzo": "Via Luigi Pirandello, 31",
        "cap": "21100",
        "citta": "Varese",
        "provincia": "VA",
        "telefono": "02 78638500",
        "lat": 45.8210, "lng": 8.8245,
        "foto_url": FOTO_POLI,
        "descrizione": (
            "Centro Medico SME, parte del gruppo CDI, a Varese. Struttura polispecialistica "
            "con ampia offerta ambulatoriale, diagnostica e riabilitativa per i residenti "
            "del varesotto e dei comuni limitrofi."
        ),
        "orari": ORARI_EXT,
        "servizi": SERV_SME,
    },
    {
        "nome": "Varese Punto Prelievi Pirandello",
        "tipo": "altro",
        "indirizzo": "Via Luigi Pirandello, 31",
        "cap": "21100",
        "citta": "Varese",
        "provincia": "VA",
        "telefono": "02 48317555",
        "lat": 45.8211, "lng": 8.8246,
        "foto_url": FOTO_LAB,
        "descrizione": "Punto prelievi SSN integrato nel Centro Medico SME di Via Pirandello.",
        "orari": ORARI_PRE,
        "servizi": SERV_PRE,
    },
    # ─── BESOZZO (VA) ────────────────────────────────────────────────────────
    {
        "nome": "CDI Besozzo Poliambulatorio",
        "tipo": "poliambulatorio",
        "indirizzo": "Via XXV Aprile, 6/F",
        "cap": "21023",
        "citta": "Besozzo",
        "provincia": "VA",
        "telefono": "02 48317555",
        "lat": 45.8714, "lng": 8.6690,
        "foto_url": FOTO_EXT,
        "descrizione": (
            "Poliambulatorio CDI a Besozzo, comune sul Lago Maggiore in provincia di Varese. "
            "Punto di riferimento per le prestazioni specialistiche nella zona del Lago Maggiore "
            "e dell'alto varesotto."
        ),
        "orari": ORARI_EXT,
        "servizi": SERV_SME,
    },
    {
        "nome": "Besozzo Punto Prelievi",
        "tipo": "altro",
        "indirizzo": "Via XXV Aprile, 6/G",
        "cap": "21023",
        "citta": "Besozzo",
        "provincia": "VA",
        "telefono": "02 48317555",
        "lat": 45.8715, "lng": 8.6691,
        "foto_url": FOTO_LAB,
        "descrizione": "Punto prelievi e poliambulatorio CDI a Besozzo, ingresso al civico 6/G.",
        "orari": ORARI_PRE,
        "servizi": SERV_PRE,
    },
]


class Command(BaseCommand):
    help = "Sostituisce le sedi di test con i centri CDI reali"

    def handle(self, *args, **kwargs):
        # Rimuovi le vecchie sedi placeholder
        vecchie = ["CDI Milano Centro", "CDI Milano Bicocca", "CDI Milano Loreto",
                   "CDI Monza", "CDI Bergamo", "CDI Brescia"]
        deleted, _ = Struttura.objects.filter(nome__in=vecchie).delete()
        if deleted:
            self.stdout.write(f"  Rimosse {deleted} sedi placeholder")

        creati = 0
        aggiornati = 0
        for data in SEDI:
            nome = data["nome"]
            _, created = Struttura.objects.update_or_create(
                nome=nome,
                defaults={**data, "attiva": True},
            )
            if created:
                creati += 1
                self.stdout.write(f"  + {nome}")
            else:
                aggiornati += 1
                self.stdout.write(f"  ~ {nome}")

        self.stdout.write(self.style.SUCCESS(
            f"\nFatto! {creati} create, {aggiornati} aggiornate."
        ))
