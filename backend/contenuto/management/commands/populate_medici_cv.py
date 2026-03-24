from django.core.management.base import BaseCommand
from contenuto.models import SchedaMedico
from prestazioni.models import Medico


MEDICI_DATA = [
    {
        "cognome": "Rossi",
        "nome": "Marco",
        "cms": {
            "nome_completo": "Dott. Marco Rossi",
            "specializzazione": "Cardiologia",
            "ruolo": "Responsabile Unità Diagnostica Cardiologica",
            "foto_url": "https://images.unsplash.com/photo-1612349317150-e413f6a5b16d?w=600&q=80&auto=format&fit=crop",
            "bio": (
                "Il Dott. Marco Rossi è cardiologo con oltre 22 anni di esperienza clinica, "
                "specializzato in diagnostica cardiovascolare non invasiva, ecocardiografia da stress "
                "e prevenzione delle malattie coronariche. Ha sviluppato un approccio integrato alla "
                "cura del paziente cardiologico, combinando l'utilizzo di tecnologie diagnostiche "
                "avanzate con una visione preventiva e personalizzata della terapia."
            ),
            "titoli_accademici": [
                {"anno": "1990", "titolo": "Laurea in Medicina e Chirurgia con lode - Universita degli Studi di Milano"},
                {"anno": "1994", "titolo": "Specializzazione in Cardiologia - Universita degli Studi di Milano"},
                {"anno": "1996", "titolo": "Fellowship in Ecocardiografia Avanzata - Centro Cardiologico Monzino, Milano"},
                {"anno": "2003", "titolo": "Master in Imaging Cardiovascolare - Universita Vita-Salute San Raffaele"},
            ],
            "esperienze_professionali": [
                {"anno": "2008 - presente", "descrizione": "Responsabile Unita Diagnostica Cardiologica - CDI Centro Diagnostico Italiano, Milano"},
                {"anno": "2001 - 2008", "descrizione": "Dirigente Medico di Cardiologia - Ospedale Niguarda Ca Granda, Milano"},
                {"anno": "1996 - 2001", "descrizione": "Medico Specialista in Cardiologia - Istituto Clinico Humanitas, Rozzano"},
                {"anno": "1994 - 1996", "descrizione": "Fellow in Cardiologia Interventistica - Centro Cardiologico Monzino"},
            ],
            "pubblicazioni": (
                "Rossi M. et al. - Valore prognostico dell'ecocardiografia da stress nella cardiopatia ischemica stabile"
                " - European Journal of Echocardiography, 2006.\n"
                "Rossi M., Colombo A. - Prevenzione cardiovascolare primaria: esperienza su 3.200 pazienti a rischio"
                " - Giornale Italiano di Cardiologia, 2011.\n"
                "Relatore al Congresso Nazionale della Societa Italiana di Cardiologia (SIC) - 2013, 2017, 2021.\n"
                "Membro del gruppo di lavoro SIC su Imaging Cardiovascolare e Prevenzione."
            ),
            "link_prenota": "/cerca?branca=cardiologia",
        },
    },
    {
        "cognome": "Bianchi",
        "nome": "Laura",
        "cms": {
            "nome_completo": "Dott.ssa Laura Bianchi",
            "specializzazione": "Ginecologia e Ostetricia",
            "ruolo": "Dirigente Medico - Responsabile Ambulatorio Ginecologico",
            "foto_url": "https://images.unsplash.com/photo-1559839734-2b71ea197ec2?w=600&q=80&auto=format&fit=crop",
            "bio": (
                "La Dott.ssa Laura Bianchi e specialista in Ginecologia e Ostetricia con 18 anni di attivita clinica. "
                "Si occupa di ginecologia preventiva, colposcopia, patologia cervicale, ecografia ostetrica e "
                "ginecologica, menopausa e medicina della riproduzione. E' particolarmente esperta nel follow-up "
                "delle lesioni pre-neoplastiche della cervice e nella gestione della gravidanza fisiologica e a rischio."
            ),
            "titoli_accademici": [
                {"anno": "1998", "titolo": "Laurea in Medicina e Chirurgia con lode - Universita degli Studi di Pavia"},
                {"anno": "2003", "titolo": "Specializzazione in Ginecologia e Ostetricia - Universita degli Studi di Milano"},
                {"anno": "2005", "titolo": "Diploma in Colposcopia avanzata - Societa Italiana di Colposcopia (SICPCV)"},
                {"anno": "2010", "titolo": "Master in Ecografia Ginecologica e Ostetrica - Fondazione IRCCS Policlinico Milano"},
            ],
            "esperienze_professionali": [
                {"anno": "2012 - presente", "descrizione": "Dirigente Medico e Responsabile Ambulatorio Ginecologico - CDI Centro Diagnostico Italiano"},
                {"anno": "2006 - 2012", "descrizione": "Medico Specialista in Ginecologia - IRCCS Istituto Europeo di Oncologia (IEO), Milano"},
                {"anno": "2003 - 2006", "descrizione": "Medico in formazione - U.O. Ginecologia, Ospedale San Gerardo di Monza"},
            ],
            "pubblicazioni": (
                "Bianchi L. et al. - Colposcopia e lesioni CIN2+: follow-up a 5 anni con trattamento LEEP"
                " - Giornale Italiano di Ostetricia e Ginecologia, 2009.\n"
                "Bianchi L., Ferrara C. - Ecografia 3D nella diagnosi delle malformazioni uterine"
                " - Journal of Obstetrics and Gynaecology, 2014.\n"
                "Relatore al Congresso Nazionale SIGO 2016 e 2020."
            ),
            "link_prenota": "/cerca?branca=ginecologia",
        },
    },
    {
        "cognome": "Ferrari",
        "nome": "Giovanni",
        "cms": {
            "nome_completo": "Dott. Giovanni Ferrari",
            "specializzazione": "Ortopedia e Traumatologia",
            "ruolo": "Dirigente Medico - Chirurgia Ortopedica e Day Surgery",
            "foto_url": "https://images.unsplash.com/photo-1582750433449-648ed127bb54?w=600&q=80&auto=format&fit=crop",
            "bio": (
                "Il Dott. Giovanni Ferrari e ortopedico con specializzazione in chirurgia artroscopica del ginocchio "
                "e della spalla, protesi d'anca e ginocchio, e traumatologia dello sport. Ha eseguito oltre 3.000 "
                "interventi chirurgici in day surgery e in regime di ricovero ordinario. E' consulente per diverse "
                "societa sportive lombarde e collabora con il centro di riabilitazione CDI per i percorsi post-operatori."
            ),
            "titoli_accademici": [
                {"anno": "1993", "titolo": "Laurea in Medicina e Chirurgia - Universita degli Studi di Bologna"},
                {"anno": "1998", "titolo": "Specializzazione in Ortopedia e Traumatologia - Universita degli Studi di Torino"},
                {"anno": "2001", "titolo": "Fellowship in Chirurgia Artroscopica - Hospital for Special Surgery, New York"},
                {"anno": "2007", "titolo": "Master in Traumatologia dello Sport - Scuola di Specializzazione di Milano"},
            ],
            "esperienze_professionali": [
                {"anno": "2010 - presente", "descrizione": "Dirigente Medico Ortopedico e Chirurgo - CDI Centro Diagnostico Italiano, Day Surgery"},
                {"anno": "2003 - 2010", "descrizione": "Chirurgo Ortopedico - U.O. Ortopedia e Traumatologia, Istituto Clinico Humanitas"},
                {"anno": "1999 - 2003", "descrizione": "Medico Specialista - Ospedale CTO, Milano (traumi complessi e chirurgia ricostruttiva)"},
            ],
            "pubblicazioni": (
                "Ferrari G. et al. - Ricostruzione del LCA con tecnica all-inside: risultati a 7 anni"
                " - Knee Surgery, Sports Traumatology, Arthroscopy, 2012.\n"
                "Ferrari G., Moretti L. - Protesi di ginocchio in paziente giovane: indicazioni e outcomes"
                " - Italian Journal of Orthopaedics and Traumatology, 2017.\n"
                "Relatore al Congresso SIOT (Societa Italiana di Ortopedia e Traumatologia) 2015, 2018, 2022."
            ),
            "link_prenota": "/cerca?branca=ortopedia",
        },
    },
    {
        "cognome": "Conti",
        "nome": "Sofia",
        "cms": {
            "nome_completo": "Dott.ssa Sofia Conti",
            "specializzazione": "Neurologia",
            "ruolo": "Responsabile Ambulatorio Neurologico e Centro Cefalee",
            "foto_url": "https://images.unsplash.com/photo-1607990281513-2c110a25bd8c?w=600&q=80&auto=format&fit=crop",
            "bio": (
                "La Dott.ssa Sofia Conti e neurologa con esperienza ultradecennale nel trattamento delle malattie "
                "neurodegenerative, epilessia, disturbi del movimento e cefalee croniche. Dirige il Centro Cefalee CDI, "
                "un servizio dedicato alla diagnosi e alla terapia multidisciplinare di emicrania, cefalea a grappolo "
                "e sindromi correlate. Ha maturato significativa esperienza nella gestione di pazienti con sclerosi "
                "multipla e nella neurofisiologia clinica."
            ),
            "titoli_accademici": [
                {"anno": "1999", "titolo": "Laurea in Medicina e Chirurgia con lode - Universita degli Studi di Padova"},
                {"anno": "2004", "titolo": "Specializzazione in Neurologia - Universita degli Studi di Milano"},
                {"anno": "2006", "titolo": "Fellowship in Sclerosi Multipla - IRCCS Fondazione Istituto Neurologico C. Besta, Milano"},
                {"anno": "2012", "titolo": "Master in Neurofisiologia Clinica - Universita degli Studi di Pavia"},
            ],
            "esperienze_professionali": [
                {"anno": "2013 - presente", "descrizione": "Responsabile Ambulatorio Neurologico e Centro Cefalee - CDI Centro Diagnostico Italiano"},
                {"anno": "2007 - 2013", "descrizione": "Medico Neurologo - U.O. Neurologia, IRCCS Fondazione Istituto Neurologico C. Besta"},
                {"anno": "2004 - 2007", "descrizione": "Specialista Ambulatoriale - Ospedale San Paolo, Milano"},
            ],
            "pubblicazioni": (
                "Conti S. et al. - Efficacia dei trattamenti preventivi nella cefalea cronica quotidiana: studio prospettico su 500 pazienti"
                " - Cephalalgia, 2010.\n"
                "Conti S., Pellegrini A. - Correlazione tra qualita del sonno e frequenza degli attacchi emicranici"
                " - Neurological Sciences, 2015.\n"
                "Membro del direttivo della Societa Italiana per lo Studio delle Cefalee (SISC) dal 2018.\n"
                "Relatore al Congresso Europeo di Neurologia (EAN) 2019 e 2023."
            ),
            "link_prenota": "/cerca?branca=neurologia",
        },
    },
    {
        "cognome": "Ricci",
        "nome": "Paolo",
        "cms": {
            "nome_completo": "Dott. Paolo Ricci",
            "specializzazione": "Radiologia e Diagnostica per Immagini",
            "ruolo": "Direttore Sanitario - Diagnostica per Immagini CDI",
            "foto_url": "https://images.unsplash.com/photo-1622253692010-333f2da6031d?w=600&q=80&auto=format&fit=crop",
            "bio": (
                "Il Dott. Paolo Ricci e radiologo con oltre 20 anni di esperienza nella diagnostica per immagini "
                "avanzata. Dirige il reparto di Radiologia CDI ed e specializzato in risonanza magnetica (RM) "
                "muscoloscheletrica e neurologica, TC multistrato, ecografia interventistica e senologia. "
                "Ha introdotto in CDI i protocolli di imaging quantitativo e la refertazione strutturata, "
                "migliorando significativamente la qualita e la riproducibilita dei referti diagnostici."
            ),
            "titoli_accademici": [
                {"anno": "1995", "titolo": "Laurea in Medicina e Chirurgia - Universita degli Studi di Milano"},
                {"anno": "2000", "titolo": "Specializzazione in Radiodiagnostica - Universita degli Studi di Milano"},
                {"anno": "2003", "titolo": "Fellowship in RM Muscoloscheletrica - Hospital for Special Surgery, New York"},
                {"anno": "2009", "titolo": "Diploma Europeo in Radiologia (EDiR) - European Society of Radiology"},
            ],
            "esperienze_professionali": [
                {"anno": "2011 - presente", "descrizione": "Direttore Sanitario Diagnostica per Immagini - CDI Centro Diagnostico Italiano"},
                {"anno": "2004 - 2011", "descrizione": "Dirigente Radiologo - U.O. Radiologia, Ospedale San Raffaele, Milano"},
                {"anno": "2000 - 2004", "descrizione": "Medico Radiologo - IRCCS Policlinico di Milano"},
            ],
            "pubblicazioni": (
                "Ricci P. et al. - RM 3T nella stadiazione delle lesioni cartilaginee del ginocchio: confronto con artroscopia"
                " - European Radiology, 2008.\n"
                "Ricci P., Grassi R. - Imaging strutturato in radiologia clinica: impatto sulla qualita diagnostica"
                " - La Radiologia Medica, 2014.\n"
                "Membro del Consiglio Direttivo della Societa Italiana di Radiologia Medica (SIRM) dal 2019.\n"
                "Autore di oltre 40 pubblicazioni su riviste internazionali indicizzate (H-index: 14)."
            ),
            "link_prenota": "/cerca?branca=radiologia",
        },
    },
    {
        "cognome": "Marino",
        "nome": "Anna",
        "cms": {
            "nome_completo": "Dott.ssa Anna Marino",
            "specializzazione": "Dermatologia e Venereologia",
            "ruolo": "Responsabile Ambulatorio Dermatologico e Centro Mappatura Neo",
            "foto_url": "https://images.unsplash.com/photo-1594824476967-48c8b964273f?w=600&q=80&auto=format&fit=crop",
            "bio": (
                "La Dott.ssa Anna Marino e dermatologa con specializzazione in dermatologia oncologica, "
                "mappatura e videodermatoscopia dei nei, diagnosi precoce del melanoma e gestione delle "
                "malattie infiammatorie croniche della cute (psoriasi, dermatite atopica). Coordina il "
                "Centro Mappatura Neo CDI, uno dei servizi piu avanzati in Lombardia per la prevenzione "
                "e la diagnosi precoce dei tumori cutanei. Collabora con il reparto di chirurgia per la "
                "gestione integrata delle lesioni sospette."
            ),
            "titoli_accademici": [
                {"anno": "2001", "titolo": "Laurea in Medicina e Chirurgia con lode - Universita degli Studi di Napoli Federico II"},
                {"anno": "2006", "titolo": "Specializzazione in Dermatologia e Venereologia - Universita degli Studi di Milano"},
                {"anno": "2008", "titolo": "Diploma in Dermatoscopia e Diagnosi del Melanoma - European Academy of Dermatology (EAD)"},
                {"anno": "2015", "titolo": "Master in Dermatologia Estetica e Laserterapia - Universita degli Studi di Roma La Sapienza"},
            ],
            "esperienze_professionali": [
                {"anno": "2014 - presente", "descrizione": "Responsabile Ambulatorio Dermatologico e Centro Mappatura Neo - CDI Centro Diagnostico Italiano"},
                {"anno": "2008 - 2014", "descrizione": "Dermatologa - U.O. Dermatologia, Fondazione IRCCS Ca Granda Ospedale Maggiore Policlinico, Milano"},
                {"anno": "2006 - 2008", "descrizione": "Specialista in Dermatologia Oncologica - Istituto Europeo di Oncologia (IEO)"},
            ],
            "pubblicazioni": (
                "Marino A. et al. - Dermatoscopia sequenziale digitale nella sorveglianza dei pazienti ad alto rischio melanoma: studio su 1.200 soggetti"
                " - Journal of the American Academy of Dermatology, 2013.\n"
                "Marino A., De Luca M. - Terapia biologica nella psoriasi moderata-grave: outcome a 3 anni in pazienti CDI"
                " - Journal of the European Academy of Dermatology and Venereology, 2019.\n"
                "Relatore al Congresso SIDeMaST (Societa Italiana di Dermatologia) 2016, 2019, 2022.\n"
                "Membro del gruppo di lavoro europeo su Melanoma Early Detection - EDF Task Force."
            ),
            "link_prenota": "/cerca?branca=dermatologia",
        },
    },
]


class Command(BaseCommand):
    help = "Crea/aggiorna i CV CMS per tutti i medici del database"

    def handle(self, *args, **kwargs):
        created = 0
        updated = 0

        for data in MEDICI_DATA:
            try:
                medico = Medico.objects.get(cognome=data["cognome"], nome=data["nome"])
            except Medico.DoesNotExist:
                self.stdout.write(self.style.WARNING(f"  Medico non trovato: {data['cognome']} {data['nome']}"))
                continue

            cms_data = {**data["cms"], "medico": medico}
            scheda, is_new = SchedaMedico.objects.update_or_create(
                nome_completo=data["cms"]["nome_completo"],
                defaults=cms_data,
            )
            # ensure the FK is set
            if scheda.medico_id != medico.id:
                scheda.medico = medico
                scheda.save(update_fields=["medico"])

            if is_new:
                created += 1
                self.stdout.write(f"  + creato: {scheda.nome_completo}")
            else:
                updated += 1
                self.stdout.write(f"  ~ aggiornato: {scheda.nome_completo}")

        self.stdout.write(self.style.SUCCESS(
            f"\nFatto! {created} creati, {updated} aggiornati."
        ))
