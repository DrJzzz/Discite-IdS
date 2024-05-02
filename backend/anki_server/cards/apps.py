from django.apps import AppConfig
from django.db.models.signals import post_migrate

class CardsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cards'
    
    def ready(self):
        from decks.models import get_default_deck
        post_migrate.connect(get_default_deck, sender=self)
        
