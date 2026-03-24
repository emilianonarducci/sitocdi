from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site
from cms.api import create_page
from cms.models import Page


class Command(BaseCommand):
    help = "Crea la struttura base delle pagine CMS"

    def handle(self, *args, **kwargs):
        # Assicura che il site sia configurato
        site = Site.objects.get_or_create(id=1, defaults={"domain": "localhost:8000", "name": "CDI"})[0]
        site.domain = "localhost:8000"
        site.name = "CDI - Centro Diagnostico Italiano"
        site.save()

        # Crea homepage se non esiste
        if not Page.objects.filter(is_home=True).exists():
            page = create_page(
                title="Home",
                template="home.html",
                language="it",
                published=True,
                in_navigation=False,
            )
            page.set_as_homepage()
            self.stdout.write(self.style.SUCCESS("Homepage creata con successo"))
        else:
            self.stdout.write("Homepage già esistente")
