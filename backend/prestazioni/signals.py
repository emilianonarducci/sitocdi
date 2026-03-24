from django.db.models.signals import post_save, post_delete, m2m_changed
from django.dispatch import receiver
from .models import Prestazione
from .search import index_prestazione, delete_prestazione


@receiver(post_save, sender=Prestazione)
def on_prestazione_save(sender, instance, **kwargs):
    try:
        index_prestazione(instance)
    except Exception:
        pass


@receiver(post_delete, sender=Prestazione)
def on_prestazione_delete(sender, instance, **kwargs):
    try:
        delete_prestazione(instance.id)
    except Exception:
        pass


@receiver(m2m_changed, sender=Prestazione.strutture.through)
@receiver(m2m_changed, sender=Prestazione.medici.through)
@receiver(m2m_changed, sender=Prestazione.fondi.through)
def on_prestazione_m2m_changed(sender, instance, **kwargs):
    if isinstance(instance, Prestazione):
        try:
            index_prestazione(instance)
        except Exception:
            pass
