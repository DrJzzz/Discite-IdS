from django.apps import AppConfig


class CardsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cards'
    
    def ready(self):
        from decks.models import get_default_deck
        get_default_deck().save()
