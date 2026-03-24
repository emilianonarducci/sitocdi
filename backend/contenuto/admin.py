from django.contrib import admin
from .models import HeroSlide, ConsigliatiCard, PercheSceglierciSezione, PercheSceglierciCard, SalutePerTeArticolo, SchedaMedico


@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ("titolo", "badge", "ordine", "attivo")
    list_editable = ("ordine", "attivo")
    list_filter = ("attivo",)


@admin.register(ConsigliatiCard)
class ConsigliatiCardAdmin(admin.ModelAdmin):
    list_display = ("titolo", "ordine", "attivo")
    list_editable = ("ordine", "attivo")


class PercheSceglierciCardInline(admin.TabularInline):
    model = PercheSceglierciCard
    extra = 0
    fields = ("ordine", "variante", "titolo", "descrizione")


@admin.register(PercheSceglierciSezione)
class PercheSceglierciSezioneAdmin(admin.ModelAdmin):
    inlines = [PercheSceglierciCardInline]


@admin.register(SalutePerTeArticolo)
class SalutePerTeArticoloAdmin(admin.ModelAdmin):
    list_display = ("titolo", "tab", "ordine", "attivo")
    list_editable = ("ordine", "attivo")
    list_filter = ("tab", "attivo")


@admin.register(SchedaMedico)
class SchedaMedicoAdmin(admin.ModelAdmin):
    list_display = ("nome_completo", "specializzazione", "ordine", "attivo")
    list_editable = ("ordine", "attivo")
    list_filter = ("attivo",)
    search_fields = ("nome_completo", "specializzazione")
    fieldsets = (
        ("Dati principali", {
            "fields": ("nome_completo", "specializzazione", "ruolo", "foto_url", "bio", "link_prenota", "attivo", "ordine"),
        }),
        ("Formazione e carriera", {
            "fields": ("titoli_accademici", "esperienze_professionali"),
            "description": (
                "Inserire come lista JSON. Titoli: [{\"anno\": \"2005\", \"titolo\": \"...\"}, ...]. "
                "Esperienze: [{\"anno\": \"2010 - presente\", \"descrizione\": \"...\"}, ...]"
            ),
        }),
        ("Ricerca e pubblicazioni", {
            "fields": ("pubblicazioni",),
        }),
    )
