from django.apps import AppConfig
from django.db.models.signals import post_migrate


class UserappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'userapp'
    
    def ready(self):
        post_migrate.connect(create_registro_on_ready, sender=self)

def create_registro_on_ready(sender, **kwargs):
    from userapp.models import get_default_user
    get_default_user()