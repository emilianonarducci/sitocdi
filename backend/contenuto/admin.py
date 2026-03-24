from django.contrib import admin
from django.utils.html import format_html
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
    list_display = ("nome_completo", "specializzazione", "ordine", "attivo", "importa_cv_link")
    list_editable = ("ordine", "attivo")
    list_filter = ("attivo",)
    search_fields = ("nome_completo", "specializzazione")

    @admin.display(description="")
    def importa_cv_link(self, obj):
        return format_html('<a href="/api/cms/upload-cv/" style="white-space:nowrap">+ Importa CV</a>')

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context["upload_cv_url"] = "/api/cms/upload-cv/"
        return super().changelist_view(request, extra_context=extra_context)

    def changeform_view(self, request, object_id=None, form_url="", extra_context=None):
        extra_context = extra_context or {}
        extra_context["upload_cv_url"] = "/api/cms/upload-cv/"
        return super().changeform_view(request, object_id, form_url, extra_context)

    change_form_template = "contenuto/schedamedico_change_form.html"

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
