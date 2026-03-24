from django.db import models


class Fondo(models.Model):
    nome = models.CharField(max_length=200)
    codice = models.CharField(max_length=50, blank=True)
    descrizione = models.TextField(blank=True)

    class Meta:
        verbose_name = "Fondo"
        verbose_name_plural = "Fondi"
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class Struttura(models.Model):
    TIPO_CHOICES = [
        ("ospedale", "Ospedale"),
        ("poliambulatorio", "Poliambulatorio"),
        ("clinica", "Clinica"),
        ("studio", "Studio medico"),
        ("altro", "Altro"),
    ]

    nome = models.CharField(max_length=200)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES, default="poliambulatorio")
    indirizzo = models.CharField(max_length=300, blank=True)
    citta = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    attiva = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Struttura"
        verbose_name_plural = "Strutture"
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class Medico(models.Model):
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    specializzazione = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    strutture = models.ManyToManyField(
        Struttura,
        related_name="medici",
        blank=True,
    )
    attivo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Medico"
        verbose_name_plural = "Medici"
        ordering = ["cognome", "nome"]

    def __str__(self):
        return f"Dr. {self.cognome} {self.nome}"

    @property
    def nome_completo(self):
        return f"Dr. {self.cognome} {self.nome}"


class Prestazione(models.Model):
    BRANCA_CHOICES = [
        ("cardiologia", "Cardiologia"),
        ("dermatologia", "Dermatologia"),
        ("ginecologia", "Ginecologia"),
        ("neurologia", "Neurologia"),
        ("oculistica", "Oculistica"),
        ("ortopedia", "Ortopedia"),
        ("otorinolaringoiatria", "Otorinolaringoiatria"),
        ("pediatria", "Pediatria"),
        ("psichiatria", "Psichiatria"),
        ("radiologia", "Radiologia"),
        ("urologia", "Urologia"),
        ("laboratorio", "Laboratorio analisi"),
        ("fisioterapia", "Fisioterapia"),
        ("chirurgia", "Chirurgia"),
        ("altra", "Altra branca"),
    ]

    nome = models.CharField(max_length=300)
    codice = models.CharField(max_length=50, blank=True, db_index=True)
    branca = models.CharField(max_length=50, choices=BRANCA_CHOICES, blank=True)
    descrizione = models.TextField(blank=True)

    # Prezzo solvente (paziente che paga di tasca propria)
    prezzo_solvente = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="Prezzo per pazienti solventi (€)",
    )

    # Strutture che erogano la prestazione
    strutture = models.ManyToManyField(
        Struttura,
        related_name="prestazioni",
        blank=True,
    )

    # Medici che erogano la prestazione
    medici = models.ManyToManyField(
        Medico,
        related_name="prestazioni",
        blank=True,
    )

    # Fondi che coprono la prestazione
    fondi = models.ManyToManyField(
        Fondo,
        related_name="prestazioni",
        blank=True,
        verbose_name="Fondi che coprono la prestazione",
    )

    attiva = models.BooleanField(default=True)
    creata_il = models.DateTimeField(auto_now_add=True)
    aggiornata_il = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Prestazione"
        verbose_name_plural = "Prestazioni"
        ordering = ["nome"]

    def __str__(self):
        return self.nome

    def coperta_da_fondo(self):
        return self.fondi.exists()
