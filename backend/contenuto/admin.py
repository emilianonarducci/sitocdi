import csv
import os
import requests
from django.contrib import admin
from django.http import HttpResponse
from django.utils.html import format_html
from .models import HeroSlide, ConsigliatiCard, PercheSceglierciSezione, PercheSceglierciCard, SalutePerTeArticolo, SchedaMedico, NewsletterIscritto


def _revalidate_medico(pk: int):
    """Chiama il frontend Next.js per invalidare la cache ISR della scheda medico."""
    frontend_url = os.environ.get("FRONTEND_URL", "").rstrip("/")
    secret = os.environ.get("REVALIDATE_SECRET", "")
    if not frontend_url or not secret:
        return
    try:
        requests.post(
            f"{frontend_url}/api/revalidate",
            json={
                "tags": ["cms-medici", f"cms-medico-{pk}"],
                "paths": [f"/medici/{pk}", "/"],
            },
            headers={"Authorization": f"Bearer {secret}"},
            timeout=5,
        )
    except Exception:
        pass


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

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        _revalidate_medico(obj.pk)

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


@admin.register(NewsletterIscritto)
class NewsletterIscrittoAdmin(admin.ModelAdmin):
    list_display = ("email", "nome", "cognome", "data_iscrizione", "attivo", "gdrive_sync_link")
    list_filter = ("attivo", "data_iscrizione")
    search_fields = ("email", "nome", "cognome")
    readonly_fields = ("data_iscrizione",)
    list_editable = ("attivo",)
    actions = ["export_csv"]

    @admin.display(description="")
    def gdrive_sync_link(self, obj):
        return format_html('<a href="/api/cms/gdrive-newsletter-sync/" style="white-space:nowrap">↺ Sync Drive</a>')

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context["gdrive_sync_url"] = "/api/cms/gdrive-newsletter-sync/"
        return super().changelist_view(request, extra_context=extra_context)

    @admin.action(description="Esporta selezionati come CSV")
    def export_csv(self, request, queryset):
        response = HttpResponse(content_type="text/csv; charset=utf-8")
        response["Content-Disposition"] = 'attachment; filename="newsletter_iscritti.csv"'
        response.write("\ufeff")  # BOM per Excel
        writer = csv.writer(response)
        writer.writerow(["Email", "Nome", "Cognome", "Data iscrizione", "Attivo"])
        for obj in queryset:
            writer.writerow([
                obj.email,
                obj.nome,
                obj.cognome,
                obj.data_iscrizione.strftime("%d/%m/%Y %H:%M"),
                "Sì" if obj.attivo else "No",
            ])
        return response
