"""
Aggiorna le foto_url di ogni sede con immagini uniche.
"""
from django.core.management.base import BaseCommand
from prestazioni.models import Struttura

# Mappa nome sede → foto_url specifica
FOTO_MAP = {
    # ── Poliambulatori CDI ──────────────────────────────────────────────────
    "CDI Saint Bon":                               "https://images.unsplash.com/photo-1586773860418-d37222d8fce3?w=800&q=80&auto=format&fit=crop",
    "CDI Fisioterapia e Riabilitazione Saint Bon": "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=800&q=80&auto=format&fit=crop",
    "CDI Dental & Face":                           "https://images.unsplash.com/photo-1588776814546-ec7e4b5c7c58?w=800&q=80&auto=format&fit=crop",
    "CDI Viale Monza":                             "https://images.unsplash.com/photo-1504813184591-01572f98c85f?w=800&q=80&auto=format&fit=crop",
    "CDI Pellegrino Rossi":                        "https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?w=800&q=80&auto=format&fit=crop",
    "CDI Cernusco sul Naviglio":                   "https://images.unsplash.com/photo-1516841273335-e39b37888115?w=800&q=80&auto=format&fit=crop",
    "CDI Corsico":                                 "https://images.unsplash.com/photo-1538108149393-fbbd81895907?w=800&q=80&auto=format&fit=crop",
    "CDI Legnano":                                 "https://images.unsplash.com/photo-1551884170-09fb70a3a2ed?w=800&q=80&auto=format&fit=crop",
    "CDI Rho":                                     "https://images.unsplash.com/photo-1576765608535-5f04d1e3f289?w=800&q=80&auto=format&fit=crop",
    "CDI Pavia":                                   "https://images.unsplash.com/photo-1579684453423-f84349ef60b0?w=800&q=80&auto=format&fit=crop",
    "CDI Varese":                                  "https://images.unsplash.com/photo-1580281657702-257584239a55?w=800&q=80&auto=format&fit=crop",
    "CDI Besozzo Poliambulatorio":                 "https://images.unsplash.com/photo-1612349317150-e413f6a5b16d?w=800&q=80&auto=format&fit=crop",
    # ── Bionics ─────────────────────────────────────────────────────────────
    "Bionics Cairoli":                             "https://images.unsplash.com/photo-1587351021759-3e566b6af7cc?w=800&q=80&auto=format&fit=crop",
    "Bionics Portello":                            "https://images.unsplash.com/photo-1632833239869-a37e3a5806d2?w=800&q=80&auto=format&fit=crop",
    "Bionics Porta Nuova":                         "https://images.unsplash.com/photo-1629909613654-28e377c37b09?w=800&q=80&auto=format&fit=crop",
    "Bionics Largo Augusto":                       "https://images.unsplash.com/photo-1666214276372-24e584975f77?w=800&q=80&auto=format&fit=crop",
    "Bionics Lavater (Porta Venezia)":             "https://images.unsplash.com/photo-1624727828489-a1e03b79bba8?w=800&q=80&auto=format&fit=crop",
    "Bionics Navigli":                             "https://images.unsplash.com/photo-1559757175-5700dde675bc?w=800&q=80&auto=format&fit=crop",
    "Bionics Viale Monza":                         "https://images.unsplash.com/photo-1631217868264-e5b90bb7e133?w=800&q=80&auto=format&fit=crop",
    "Bionics Bicocca":                             "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=800&q=80&auto=format&fit=crop",
    "Bionics Citylife":                            "https://images.unsplash.com/photo-1530026405186-ed1f139313f8?w=800&q=80&auto=format&fit=crop",
    "Bionics Symbiosis":                           "https://images.unsplash.com/photo-1581595220892-b0739db3ba8c?w=800&q=80&auto=format&fit=crop",
    "Centro Medico SME Varese":                    "https://images.unsplash.com/photo-1516549655169-df83a0774514?w=800&q=80&auto=format&fit=crop",
    # ── Punti prelievi ──────────────────────────────────────────────────────
    "Portello Punto Prelievi":                     "https://images.unsplash.com/photo-1579684385127-1ef15d508118?w=800&q=80&auto=format&fit=crop",
    "Bicocca Punto Prelievi SSN":                  "https://images.unsplash.com/photo-1631815588090-d4bfec5b1ccb?w=800&q=80&auto=format&fit=crop",
    "Citylife Punto Prelievi SSN":                 "https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=800&q=80&auto=format&fit=crop",
    "Abruzzi Punto Prelievi SSN":                  "https://images.unsplash.com/photo-1584820927498-cfe5211fd8bf?w=800&q=80&auto=format&fit=crop",
    "Corso Italia Punto Prelievi SSN":             "https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=800&q=80&auto=format&fit=crop",
    "Giulio Romano Punto Prelievi SSN":            "https://images.unsplash.com/photo-1505751172876-fa1923c5c528?w=800&q=80&auto=format&fit=crop",
    "Navigli Punto Prelievi SSN":                  "https://images.unsplash.com/photo-1532938911079-1b06ac7ceec7?w=800&q=80&auto=format&fit=crop",
    "Symbiosis Punto Prelievi SSN":                "https://images.unsplash.com/photo-1516841273335-e39b37888115?w=800&q=80&auto=format&fit=crop",
    "Varese Punto Prelievi Pirandello":            "https://images.unsplash.com/photo-1530026186672-2cd00ffc50fe?w=800&q=80&auto=format&fit=crop",
    "Besozzo Punto Prelievi":                      "https://images.unsplash.com/photo-1551884170-09fb70a3a2ed?w=800&q=80&auto=format&fit=crop",
}


class Command(BaseCommand):
    help = "Aggiorna foto_url di ogni sede con immagini uniche"

    def handle(self, *args, **options):
        updated = 0
        not_found = []

        for nome, foto_url in FOTO_MAP.items():
            count = Struttura.objects.filter(nome=nome).update(foto_url=foto_url)
            if count:
                updated += count
                self.stdout.write(f"  ✓ {nome}")
            else:
                not_found.append(nome)

        self.stdout.write(self.style.SUCCESS(f"\nAggiornate {updated} sedi."))
        if not_found:
            self.stdout.write(self.style.WARNING(f"Non trovate: {', '.join(not_found)}"))
