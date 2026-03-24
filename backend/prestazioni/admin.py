from django.contrib import admin
from .models import Fondo, Struttura, Medico, Prestazione


@admin.register(Fondo)
class FondoAdmin(admin.ModelAdmin):
    list_display = ["nome", "codice"]
    search_fields = ["nome", "codice"]


@admin.register(Struttura)
class StrutturaAdmin(admin.ModelAdmin):
    list_display = ["nome", "tipo", "citta", "attiva"]
    list_filter = ["tipo", "attiva"]
    search_fields = ["nome", "citta"]


@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ["cognome", "nome", "specializzazione", "attivo"]
    list_filter = ["attivo", "specializzazione"]
    search_fields = ["nome", "cognome", "specializzazione"]
    filter_horizontal = ["strutture"]


@admin.register(Prestazione)
class PrestazioneAdmin(admin.ModelAdmin):
    list_display = ["nome", "codice", "branca", "prezzo_solvente", "coperta_da_fondo", "attiva"]
    list_filter = ["branca", "attiva", "fondi"]
    search_fields = ["nome", "codice", "descrizione"]
    filter_horizontal = ["strutture", "medici", "fondi"]
