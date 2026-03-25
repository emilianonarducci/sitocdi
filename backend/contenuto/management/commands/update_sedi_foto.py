"""
Aggiorna le foto_url di ogni sede con immagini uniche.
"""
from django.core.management.base import BaseCommand
from prestazioni.models import Struttura

# Mappa nome sede → foto_url specifica
FOTO_MAP = {
    "CDI Saint Bon":                          "https://www.cdi.it/wp-content/uploads/2019/09/CDI-Saint-Bon.jpg",
    "CDI Fisioterapia e Riabilitazione Saint Bon": "https://www.cdi.it/wp-content/uploads/2019/09/CDI-Fisioterapia-Saint-Bon.jpg",
    "CDI Dental & Face":                      "https://www.cdi.it/wp-content/uploads/2019/09/CDI-Dental-Face.jpg",
    "Bionics Cairoli":                        "https://www.cdi.it/wp-content/uploads/2019/09/Bionics-Cairoli.jpg",
    "Bionics Portello":                       "https://www.cdi.it/wp-content/uploads/2019/09/Bionics-Portello.jpg",
    "Bionics Porta Nuova":                    "https://www.cdi.it/wp-content/uploads/2019/09/Bionics-Porta-Nuova.jpg",
    "Bionics Largo Augusto":                  "https://www.cdi.it/wp-content/uploads/2019/09/Bionics-Largo-Augusto.jpg",
    "Bionics Lavater (Porta Venezia)":        "https://www.cdi.it/wp-content/uploads/2019/09/Bionics-Lavater.jpg",
    "Bionics Navigli":                        "https://www.cdi.it/wp-content/uploads/2019/09/Bionics-Navigli.jpg",
    "Bionics Viale Monza":                    "https://www.cdi.it/wp-content/uploads/2019/09/Bionics-Viale-Monza.jpg",
    "CDI Viale Monza":                        "https://www.cdi.it/wp-content/uploads/2019/09/CDI-Viale-Monza.jpg",
    "Bionics Bicocca":                        "https://www.cdi.it/wp-content/uploads/2019/09/Bionics-Bicocca.jpg",
    "Bionics Citylife":                       "https://www.cdi.it/wp-content/uploads/2019/09/Bionics-Citylife.jpg",
    "CDI Pellegrino Rossi":                   "https://www.cdi.it/wp-content/uploads/2019/09/CDI-Pellegrino-Rossi.jpg",
    "Bionics Symbiosis":                      "https://www.cdi.it/wp-content/uploads/2019/09/Bionics-Symbiosis.jpg",
    "CDI Cernusco sul Naviglio":              "https://www.cdi.it/wp-content/uploads/2019/09/CDI-Cernusco.jpg",
    "CDI Corsico":                            "https://www.cdi.it/wp-content/uploads/2019/09/CDI-Corsico.jpg",
    "CDI Legnano":                            "https://www.cdi.it/wp-content/uploads/2019/09/CDI-Legnano.jpg",
    "CDI Rho":                                "https://www.cdi.it/wp-content/uploads/2019/09/CDI-Rho.jpg",
    "CDI Pavia":                              "https://www.cdi.it/wp-content/uploads/2019/09/CDI-Pavia.jpg",
    "CDI Varese":                             "https://www.cdi.it/wp-content/uploads/2022/10/CDI-Varese.jpg",
    "Centro Medico SME Varese":               "https://www.cdi.it/wp-content/uploads/2022/10/SME-Varese.jpg",
    "CDI Besozzo Poliambulatorio":            "https://www.cdi.it/wp-content/uploads/2022/10/CDI-Besozzo.jpg",
    # Punti prelievi — foto stock diverse per ciascuno
    "Portello Punto Prelievi":                "https://images.unsplash.com/photo-1579684385127-1ef15d508118?w=800&q=80&auto=format&fit=crop",
    "Bicocca Punto Prelievi SSN":             "https://images.unsplash.com/photo-1631815588090-d4bfec5b1ccb?w=800&q=80&auto=format&fit=crop",
    "Citylife Punto Prelievi SSN":            "https://images.unsplash.com/photo-1581595220892-b0739db3ba8c?w=800&q=80&auto=format&fit=crop",
    "Abruzzi Punto Prelievi SSN":             "https://images.unsplash.com/photo-1584820927498-cfe5211fd8bf?w=800&q=80&auto=format&fit=crop",
    "Corso Italia Punto Prelievi SSN":        "https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=800&q=80&auto=format&fit=crop",
    "Giulio Romano Punto Prelievi SSN":       "https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=800&q=80&auto=format&fit=crop",
    "Navigli Punto Prelievi SSN":             "https://images.unsplash.com/photo-1505751172876-fa1923c5c528?w=800&q=80&auto=format&fit=crop",
    "Symbiosis Punto Prelievi SSN":           "https://images.unsplash.com/photo-1530026405186-ed1f139313f8?w=800&q=80&auto=format&fit=crop",
    "Varese Punto Prelievi Pirandello":       "https://images.unsplash.com/photo-1516549655169-df83a0774514?w=800&q=80&auto=format&fit=crop",
    "Besozzo Punto Prelievi":                 "https://images.unsplash.com/photo-1666214276372-24e584975f77?w=800&q=80&auto=format&fit=crop",
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
