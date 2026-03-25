"""
Aggiorna le foto_url di ogni sede con immagini uniche.
"""
from django.core.management.base import BaseCommand
from prestazioni.models import Struttura

# Mappa nome sede → foto_url specifica
FOTO_MAP = {
    # ── Poliambulatori CDI — foto reali dal sito cdi.it ────────────────────
    "CDI Saint Bon":                               "https://www.cdi.it/wp-content/uploads/2019/09/sede-CDI-Saint-Bon.jpg",
    "CDI Fisioterapia e Riabilitazione Saint Bon": "https://www.cdi.it/wp-content/uploads/2023/12/IMG_1399-scaled-1024x1024.jpg",
    "CDI Dental & Face":                           "https://www.cdi.it/wp-content/uploads/2023/12/6-1-scaled-1024x1024.jpg",
    "CDI Viale Monza":                             "https://www.cdi.it/wp-content/uploads/2023/12/20231025_145806-scaled-1024x1024.jpg",
    "CDI Pellegrino Rossi":                        "https://www.cdi.it/wp-content/uploads/2019/09/10.jpg",
    "CDI Pavia":                                   "https://www.cdi.it/wp-content/uploads/2023/01/7-1024x1024.jpg",
    "CDI Varese":                                  "https://www.cdi.it/wp-content/uploads/2019/09/Varese-portici.jpg",
    "CDI Cernusco sul Naviglio":                   "https://www.cdi.it/wp-content/uploads/2023/01/8-1024x1024.jpg",
    "CDI Corsico":                                 "https://www.cdi.it/wp-content/uploads/2023/01/10-1024x1024.jpg",
    "CDI Legnano":                                 "https://www.cdi.it/wp-content/uploads/2023/01/13-scaled-1024x1024.jpg",
    "CDI Rho":                                     "https://www.cdi.it/wp-content/uploads/2019/09/laterale-edificio-cdi.jpg",
    "CDI Besozzo Poliambulatorio":                 "https://www.cdi.it/wp-content/uploads/2021/02/IMG_E2807-640x480-1.jpg",
    "Centro Medico SME Varese":                    "https://www.cdi.it/wp-content/uploads/2021/02/IMG_E2826-640x480-1.jpg",
    # ── Bionics — foto reali dal sito cdi.it ───────────────────────────────
    "Bionics Cairoli":                             "https://www.cdi.it/wp-content/uploads/2023/12/D4D5AD05-D9DF-401A-A28A-5391B9F19F75-scaled-1024x1024.jpeg",
    "Bionics Portello":                            "https://www.cdi.it/wp-content/uploads/2019/09/ingresso-CDI.png",
    "Bionics Porta Nuova":                         "https://www.cdi.it/wp-content/uploads/2023/12/CDI-Porta-Nuova-interni-scaled-1024x1024.jpg",
    "Bionics Largo Augusto":                       "https://www.cdi.it/wp-content/uploads/2023/12/329C1B3D-ABA3-4893-A58A-311B10BEB911-scaled-1024x1024.jpeg",
    "Bionics Lavater (Porta Venezia)":             "https://www.cdi.it/wp-content/uploads/2023/12/B5024B00-2BE1-4B12-95EB-FB78EB42CD81-scaled-1024x1024.jpeg",
    "Bionics Navigli":                             "https://www.cdi.it/wp-content/uploads/2020/12/IMG_2555-800x600-1.jpg",
    "Bionics Viale Monza":                         "https://www.cdi.it/wp-content/uploads/2023/12/5-1-scaled-1024x1024.jpg",
    "Bionics Bicocca":                             "https://www.cdi.it/wp-content/uploads/2021/08/IMG_4800-800x600-1.jpg",
    "Bionics Citylife":                            "https://www.cdi.it/wp-content/uploads/2021/02/IMG_8982-800x592-1.jpg",
    "Bionics Symbiosis":                           "https://www.cdi.it/wp-content/uploads/2021/02/IMG_8988-800x600-1.jpg",
    # ── Punti prelievi — foto interne CDI ──────────────────────────────────
    "Portello Punto Prelievi":                     "https://www.cdi.it/wp-content/uploads/2023/12/IMG_2403-scaled-1024x1024.jpeg",
    "Bicocca Punto Prelievi SSN":                  "https://www.cdi.it/wp-content/uploads/2021/08/IMG_4807-800x600-2.jpg",
    "Citylife Punto Prelievi SSN":                 "https://www.cdi.it/wp-content/uploads/2021/02/IMG_9004-800x600-1.jpg",
    "Abruzzi Punto Prelievi SSN":                  "https://www.cdi.it/wp-content/uploads/2021/08/IMG_4814-800x600-2.jpg",
    "Corso Italia Punto Prelievi SSN":             "https://www.cdi.it/wp-content/uploads/2021/02/IMG_2570-800x597-1.jpg",
    "Giulio Romano Punto Prelievi SSN":            "https://www.cdi.it/wp-content/uploads/2021/02/IMG_2554-800x600-1.jpg",
    "Navigli Punto Prelievi SSN":                  "https://www.cdi.it/wp-content/uploads/2021/02/IMG_2575-800x613-1.jpg",
    "Symbiosis Punto Prelievi SSN":                "https://www.cdi.it/wp-content/uploads/2021/08/IMG_4818-800x600-1.jpg",
    "Varese Punto Prelievi Pirandello":            "https://www.cdi.it/wp-content/uploads/2021/02/IMG_2810-640x480-1.jpg",
    "Besozzo Punto Prelievi":                      "https://www.cdi.it/wp-content/uploads/2021/08/IMG_4821-800x600-2.jpg",
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
