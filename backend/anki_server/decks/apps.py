from django.apps import AppConfig
from django.db.models.signals import post_migrate


class DecksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'decks'

    def ready(self):
        from userapp.models import get_default_user
        get_default_user().save()
        #post_migrate.connect(create_registro_on_ready, sender=self)

def create_registro_on_ready(sender, **kwargs):
    from decks.models import get_default_deck
    get_default_deck().save()