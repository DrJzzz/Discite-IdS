from django.apps import AppConfig
from django.db.models.signals import post_migrate

class ImagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'images'
    
    def ready(self):
        from userapp.models import get_default_user
        post_migrate.connect(get_default_user, sender=self)
