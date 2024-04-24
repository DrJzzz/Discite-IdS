from django.apps import AppConfig
from django.db.models.signals import post_migrate


class DecksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'decks'

    def ready(self):
        post_migrate.connect(create_registro_on_ready, sender=self)

def create_registro_on_ready(sender, **kwargs):
    from .models import create_deck
    create_deck()