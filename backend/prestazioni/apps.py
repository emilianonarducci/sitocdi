from django.apps import AppConfig


class PrestazioniConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "prestazioni"
    verbose_name = "Prestazioni Mediche"

    def ready(self):
        import prestazioni.signals  # noqa
