from django.contrib import admin
from .models import HeroSlide, ConsigliatiCard, PercheSceglierciSezione, PercheSceglierciCard, SalutePerTeArticolo


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
