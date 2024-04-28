from django.apps import AppConfig
from django.db.models.signals import post_migrate


class DecksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'decks'

    def ready(self):
        from userapp.models import get_default_user
        get_default_user().save()
        
