from django.core.management.base import BaseCommand
from contenuto.models import (
    HeroSlide, ConsigliatiCard,
    PercheSceglierciSezione, PercheSceglierciCard,
    SalutePerTeArticolo, SchedaMedico,
)


class Command(BaseCommand):
    help = "Popola il CMS con contenuti di esempio"

    def handle(self, *args, **kwargs):

        # ── Hero slides ──────────────────────────────────────────
        self.stdout.write("Creazione slide Hero...")
        slides = [
            {
                "badge": "CDI — Dal 1975",
                "titolo": "La tua salute,\nla nostra missione.",
                "sottotitolo": "Oltre 80 centri in Lombardia. Prenota visite, esami e prestazioni mediche con i migliori specialisti.",
                "cta_testo": "Prenota ora",
                "cta_link": "/cerca",
                "immagine_url": "https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=1600&q=80&auto=format&fit=crop",
                "ordine": 0,
            },
            {
                "badge": "Innovazione",
                "titolo": "Tecnologie diagnostiche\nall'avanguardia.",
                "sottotitolo": "RMN, TAC, PET e molto altro. Diagnosi precise per cure efficaci.",
                "cta_testo": "Scopri i servizi",
                "cta_link": "/cerca",
                "immagine_url": "https://images.unsplash.com/photo-1516069677018-378515003435?w=1600&q=80&auto=format&fit=crop",
                "ordine": 1,
            },
            {
                "badge": "Fondi sanitari",
                "titolo": "Convenzionati con\ni principali fondi.",
                "sottotitolo": "FASI, Metasalute, FASDAC, Previmedical, Unisalute e molti altri. Verifica la tua copertura.",
                "cta_testo": "Verifica copertura",
                "cta_link": "/cerca",
                "immagine_url": "https://images.unsplash.com/photo-1579684385127-1ef15d508118?w=1600&q=80&auto=format&fit=crop",
                "ordine": 2,
            },
        ]
        for s in slides:
            HeroSlide.objects.get_or_create(titolo=s["titolo"], defaults=s)
        self.stdout.write(f"  ✓ {len(slides)} slide")

        # ── Consigliati per te ───────────────────────────────────
        self.stdout.write("Creazione card Consigliati per te...")
        consigliati = [
            {
                "titolo": "Visita cardiologica",
                "immagine_url": "https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=300&q=80&auto=format&fit=crop",
                "link": "/cerca?q=visita+cardiologica",
                "ordine": 0,
            },
            {
                "titolo": "Esami del sangue",
                "immagine_url": "https://images.unsplash.com/photo-1532187863486-abf9dbad1b69?w=300&q=80&auto=format&fit=crop",
                "link": "/cerca?q=esame+sangue",
                "ordine": 1,
            },
            {
                "titolo": "Ecografia",
                "immagine_url": "https://images.unsplash.com/photo-1576671081837-49000212a370?w=300&q=80&auto=format&fit=crop",
                "link": "/cerca?q=ecografia",
                "ordine": 2,
            },
        ]
        for c in consigliati:
            ConsigliatiCard.objects.get_or_create(titolo=c["titolo"], defaults=c)
        self.stdout.write(f"  ✓ {len(consigliati)} card")

        # ── Perché sceglierci ────────────────────────────────────
        self.stdout.write("Creazione sezione Perché sceglierci...")
        sezione, _ = PercheSceglierciSezione.objects.get_or_create(
            titolo="Perché sceglierci",
            defaults={
                "descrizione": "Ascoltare e comprenderne le esigenze, ricercare con continuità la personalizzazione del \"servizio\" e offrire la migliore soluzione per soddisfarne le aspettative.",
                "immagine_sfondo_url": "https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=1600&q=80&auto=format&fit=crop",
            }
        )
        cards_perche = [
            {"variante": "light", "titolo": "Innovazione", "descrizione": "Il CDI investe costantemente in tecnologie diagnostiche avanzate, soluzioni digitali e ricerca clinica per garantire esami di qualità.", "ordine": 0},
            {"variante": "mid", "titolo": "+80 Centri in Lombardia", "descrizione": "Siamo presenti sul territorio lombardo con oltre 80 sedi, di cui 22 poliambulatori.", "ordine": 1},
            {"variante": "dark", "titolo": "Eccellenza clinica", "descrizione": "Fare della ricerca costante dell'eccellenza clinica e dello sviluppo tecnologico il carattere distintivo di CDI.", "ordine": 2},
        ]
        for c in cards_perche:
            PercheSceglierciCard.objects.get_or_create(sezione=sezione, titolo=c["titolo"], defaults=c)
        self.stdout.write("  ✓ sezione + 3 card")

        # ── Salute per te ────────────────────────────────────────
        self.stdout.write("Creazione articoli Salute per te...")
        articoli = [
            {"tab": "Consigli e approfondimenti", "titolo": "Benessere in viaggio: tutti i consigli", "descrizione": "Dalle mete ideali agli accorgimenti per la tua salute.", "immagine_url": "https://images.unsplash.com/photo-1501700493788-fa1a4fc9fe62?w=400&q=80&auto=format&fit=crop", "ordine": 0},
            {"tab": "Consigli e approfondimenti", "titolo": "CDI per le donne", "descrizione": "Percorsi di prevenzione, diagnosi e cura pensati per la salute femminile.", "immagine_url": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=400&q=80&auto=format&fit=crop", "ordine": 1},
            {"tab": "Consigli e approfondimenti", "titolo": "È arrivata la tariffa YOUNG", "descrizione": "Per i pazienti di età compresa tra i 18 e i 30 anni.", "immagine_url": "https://images.unsplash.com/photo-1529156069898-49953e39b3ac?w=400&q=80&auto=format&fit=crop", "ordine": 2},
            {"tab": "Consigli e approfondimenti", "titolo": "Come avvicinare i bambini agli sport invernali", "descrizione": "Alcuni consigli da seguire affinché i nostri figli possano divertirsi.", "immagine_url": "https://images.unsplash.com/photo-1551698618-1dfe5d97d256?w=400&q=80&auto=format&fit=crop", "ordine": 3},
            {"tab": "News", "titolo": "CDI amplia i servizi di cardiologia", "descrizione": "Nuovi macchinari di ultima generazione disponibili nelle sedi di Milano.", "immagine_url": "https://images.unsplash.com/photo-1504813184591-01572f98c85f?w=400&q=80&auto=format&fit=crop", "ordine": 0},
            {"tab": "News", "titolo": "Nuova sede a Bergamo", "descrizione": "Apriamo un nuovo poliambulatorio nel cuore di Bergamo.", "immagine_url": "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=400&q=80&auto=format&fit=crop", "ordine": 1},
            {"tab": "News", "titolo": "CDI e la ricerca oncologica", "descrizione": "Il nostro impegno nella diagnosi precoce dei tumori.", "immagine_url": "https://images.unsplash.com/photo-1586773860418-d37222d8fce3?w=400&q=80&auto=format&fit=crop", "ordine": 2},
            {"tab": "News", "titolo": "Accordo con i principali fondi sanitari", "descrizione": "Ampliata la copertura per FASI, Metasalute e Unisalute.", "immagine_url": "https://images.unsplash.com/photo-1532938911079-1b06ac7ceec7?w=400&q=80&auto=format&fit=crop", "ordine": 3},
            {"tab": "Comunicati stampa", "titolo": "CDI ottiene la certificazione ISO 9001", "descrizione": "Ulteriore riconoscimento della qualità dei nostri servizi sanitari.", "immagine_url": "https://images.unsplash.com/photo-1568667256549-094345857637?w=400&q=80&auto=format&fit=crop", "ordine": 0},
            {"tab": "Comunicati stampa", "titolo": "Partnership con l'Università di Milano", "descrizione": "Firmato accordo per la ricerca e la formazione medica.", "immagine_url": "https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?w=400&q=80&auto=format&fit=crop", "ordine": 1},
            {"tab": "Articoli", "titolo": "Alimentazione e prevenzione", "descrizione": "Come una dieta equilibrata riduce il rischio di malattie croniche.", "immagine_url": "https://images.unsplash.com/photo-1498837167922-ddd27525d352?w=400&q=80&auto=format&fit=crop", "ordine": 0},
            {"tab": "Articoli", "titolo": "Attività fisica dopo i 50 anni", "descrizione": "Consigli pratici per mantenersi in forma in ogni fase della vita.", "immagine_url": "https://images.unsplash.com/photo-1571019614242-c5c5dee9f50b?w=400&q=80&auto=format&fit=crop", "ordine": 1},
        ]
        for a in articoli:
            SalutePerTeArticolo.objects.get_or_create(titolo=a["titolo"], defaults=a)
        self.stdout.write(f"  ✓ {len(articoli)} articoli")

        # ── Schede Medici ─────────────────────────────────────────
        self.stdout.write("Creazione schede medici...")
        medici = [
            {
                "nome_completo": "Dott.ssa Ileana Abbiati",
                "specializzazione": "Ginecologia e Ostetricia",
                "ruolo": "Dirigente Medico – Responsabile Ambulatorio Ginecologico",
                "foto_url": "https://images.unsplash.com/photo-1559839734-2b71ea197ec2?w=600&q=80&auto=format&fit=crop",
                "bio": (
                    "La Dott.ssa Ileana Abbiati è specialista in Ginecologia e Ostetricia con oltre 20 anni "
                    "di esperienza clinica. Si occupa di ginecologia preventiva, patologia cervicale, "
                    "ecografia ostetrica e ginecologica, menopausa e contraccezione. Ha maturato una "
                    "significativa esperienza in colposcopia e nel trattamento delle lesioni pre-neoplastiche "
                    "della cervice uterina."
                ),
                "titoli_accademici": [
                    {"anno": "1990", "titolo": "Laurea in Medicina e Chirurgia – Università degli Studi di Milano, con lode"},
                    {"anno": "1994", "titolo": "Specializzazione in Ginecologia e Ostetricia – Università degli Studi di Milano"},
                    {"anno": "1996", "titolo": "Master in Ecografia Ostetrica e Ginecologica – Fondazione IRCCS Policlinico"},
                    {"anno": "2002", "titolo": "Diploma in Colposcopia avanzata – Società Italiana di Colposcopia e Patologia Cervico-Vaginale (SICPCV)"},
                ],
                "esperienze_professionali": [
                    {"anno": "2005 – presente", "descrizione": "Dirigente Medico e Responsabile Ambulatorio Ginecologico – CDI Centro Diagnostico Italiano, Milano"},
                    {"anno": "1999 – 2005", "descrizione": "Medico Specialista – IRCCS Istituto Europeo di Oncologia (IEO), Unità di Ginecologia Oncologica"},
                    {"anno": "1994 – 1999", "descrizione": "Medico in formazione specialistica – U.O. Ginecologia e Ostetricia, Ospedale San Raffaele, Milano"},
                ],
                "pubblicazioni": (
                    "Abbiati I. et al. - Colposcopia e lesioni CIN2+: follow-up a 5 anni in pazienti trattate con LEEP"
                    " - Giornale Italiano di Ostetricia e Ginecologia, 2008.\n"
                    "Abbiati I., Rossi M. - Ecografia tridimensionale nella diagnosi delle malformazioni uterine"
                    " - Journal of Obstetrics and Gynaecology Research, 2012.\n"
                    "Partecipazione come relatore al Congresso Nazionale SIGO 2015 e 2019."
                ),
                "link_prenota": "/cerca?branca=ginecologia",
                "attivo": True,
                "ordine": 0,
            },
            {
                "nome_completo": "Dott. Marco Ferrari",
                "specializzazione": "Cardiologia",
                "ruolo": "Responsabile Unità Diagnostica Cardiologica",
                "foto_url": "https://images.unsplash.com/photo-1612349317150-e413f6a5b16d?w=600&q=80&auto=format&fit=crop",
                "bio": (
                    "Il Dott. Marco Ferrari è cardiologo con specializzazione in diagnostica non invasiva. "
                    "Si occupa di ecocardiografia, holter cardiaco, ergometria e prevenzione cardiovascolare. "
                    "Ha una lunga esperienza nel trattamento delle cardiopatie coronariche e nello scompenso cardiaco."
                ),
                "titoli_accademici": [
                    {"anno": "1988", "titolo": "Laurea in Medicina e Chirurgia – Università degli Studi di Pavia"},
                    {"anno": "1992", "titolo": "Specializzazione in Cardiologia – Università degli Studi di Milano"},
                    {"anno": "1995", "titolo": "Fellowship in Ecocardiografia Avanzata – Centro Cardiologico Monzino"},
                ],
                "esperienze_professionali": [
                    {"anno": "2008 – presente", "descrizione": "Responsabile Unità Diagnostica Cardiologica – CDI Centro Diagnostico Italiano"},
                    {"anno": "1998 – 2008", "descrizione": "Dirigente Medico – U.O. Cardiologia, Ospedale Niguarda Ca' Granda, Milano"},
                    {"anno": "1992 – 1998", "descrizione": "Medico Specialista in Cardiologia – Istituto Clinico Humanitas"},
                ],
                "pubblicazioni": (
                    "Ferrari M. et al. - Valore prognostico dell'ecocardiografia da stress nella cardiopatia ischemica stabile"
                    " - European Journal of Echocardiography, 2005.\n"
                    "Ferrari M. - Prevenzione cardiovascolare primaria: esperienza CDI su 3000 pazienti"
                    " - Atti del 75 Congresso Nazionale della Societa Italiana di Cardiologia, 2014."
                ),
                "link_prenota": "/cerca?branca=cardiologia",
                "attivo": True,
                "ordine": 1,
            },
        ]
        for m in medici:
            SchedaMedico.objects.get_or_create(nome_completo=m["nome_completo"], defaults=m)
        self.stdout.write(f"  ✓ {len(medici)} schede medici")

        self.stdout.write(self.style.SUCCESS("\nCMS popolato con successo!"))
