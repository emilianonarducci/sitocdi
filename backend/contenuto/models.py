from django.db import models
from django.db.models import JSONField


class HeroSlide(models.Model):
    badge = models.CharField("Badge", max_length=100, default="CDI")
    titolo = models.CharField("Titolo", max_length=200)
    sottotitolo = models.TextField("Sottotitolo")
    cta_testo = models.CharField("Testo bottone", max_length=50, default="Prenota ora")
    cta_link = models.CharField("Link bottone", max_length=200, default="/cerca")
    immagine_url = models.URLField("URL immagine", max_length=500)
    ordine = models.PositiveIntegerField("Ordine", default=0)
    attivo = models.BooleanField("Attivo", default=True)

    class Meta:
        ordering = ["ordine"]
        verbose_name = "Slide Hero"
        verbose_name_plural = "Slide Hero"

    def __str__(self):
        return self.titolo


class ConsigliatiCard(models.Model):
    titolo = models.CharField("Titolo", max_length=200)
    immagine_url = models.URLField("URL immagine", max_length=500)
    link = models.CharField("Link", max_length=200, default="#")
    ordine = models.PositiveIntegerField("Ordine", default=0)
    attivo = models.BooleanField("Attivo", default=True)

    class Meta:
        ordering = ["ordine"]
        verbose_name = "Card Consigliati per te"
        verbose_name_plural = "Card Consigliati per te"

    def __str__(self):
        return self.titolo


class PercheSceglierciSezione(models.Model):
    titolo = models.CharField("Titolo sezione", max_length=200, default="Perché sceglierci")
    descrizione = models.TextField("Descrizione")
    immagine_sfondo_url = models.URLField("URL immagine sfondo", max_length=500)

    class Meta:
        verbose_name = "Sezione Perché Sceglierci"
        verbose_name_plural = "Sezione Perché Sceglierci"

    def __str__(self):
        return self.titolo


class PercheSceglierciCard(models.Model):
    VARIANT_CHOICES = [
        ("light", "Chiara (bianca)"),
        ("mid", "Blu medio"),
        ("dark", "Blu scuro"),
    ]
    sezione = models.ForeignKey(
        PercheSceglierciSezione, on_delete=models.CASCADE, related_name="cards"
    )
    variante = models.CharField("Variante", max_length=10, choices=VARIANT_CHOICES, default="light")
    titolo = models.CharField("Titolo", max_length=200)
    descrizione = models.TextField("Descrizione")
    ordine = models.PositiveIntegerField("Ordine", default=0)

    class Meta:
        ordering = ["ordine"]
        verbose_name = "Card Perché Sceglierci"
        verbose_name_plural = "Card Perché Sceglierci"

    def __str__(self):
        return self.titolo


class SalutePerTeArticolo(models.Model):
    TAB_CHOICES = [
        ("Consigli e approfondimenti", "Consigli e approfondimenti"),
        ("News", "News"),
        ("Comunicati stampa", "Comunicati stampa"),
        ("Articoli", "Articoli"),
    ]
    tab = models.CharField("Tab", max_length=50, choices=TAB_CHOICES)
    titolo = models.CharField("Titolo", max_length=200)
    descrizione = models.TextField("Descrizione")
    immagine_url = models.URLField("URL immagine", max_length=500)
    link = models.CharField("Link", max_length=200, default="#")
    ordine = models.PositiveIntegerField("Ordine", default=0)
    attivo = models.BooleanField("Attivo", default=True)

    class Meta:
        ordering = ["tab", "ordine"]
        verbose_name = "Articolo Salute per te"
        verbose_name_plural = "Articoli Salute per te"

    def __str__(self):
        return f"[{self.tab}] {self.titolo}"


class SchedaMedico(models.Model):
    medico = models.OneToOneField(
        "prestazioni.Medico",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="scheda_cms",
        verbose_name="Medico collegato",
        help_text="Collega questa scheda al medico nel catalogo prestazioni",
    )
    nome_completo = models.CharField("Nome completo", max_length=200, help_text="Es: Dott.ssa Ileana Abbiati")
    specializzazione = models.CharField("Specializzazione", max_length=300, help_text="Es: Ginecologia e Ostetricia")
    ruolo = models.CharField("Ruolo / Qualifica", max_length=300, blank=True, help_text="Es: Dirigente Medico - Responsabile ambulatorio")
    foto_url = models.URLField("URL foto", max_length=500, blank=True)
    bio = models.TextField("Biografia / Presentazione", blank=True, help_text="Testo introduttivo visualizzato nella scheda")
    titoli_accademici = JSONField(
        "Titoli accademici",
        default=list,
        blank=True,
        help_text='Lista JSON: [{"anno": "2005", "titolo": "Specializzazione in Ginecologia"}, ...]',
    )
    esperienze_professionali = JSONField(
        "Esperienze professionali",
        default=list,
        blank=True,
        help_text='Lista JSON: [{"anno": "2010 - presente", "descrizione": "Dirigente medico CDI"}, ...]',
    )
    pubblicazioni = models.TextField("Pubblicazioni e Ricerca", blank=True, help_text="Testo libero su pubblicazioni e attività di ricerca")
    link_prenota = models.CharField("Link prenota", max_length=200, default="/cerca", blank=True)
    attivo = models.BooleanField("Attivo", default=True)
    ordine = models.PositiveIntegerField("Ordine", default=0)

    class Meta:
        ordering = ["ordine", "nome_completo"]
        verbose_name = "Scheda Medico"
        verbose_name_plural = "Schede Medici"

    def __str__(self):
        return self.nome_completo
