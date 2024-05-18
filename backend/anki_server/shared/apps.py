from django.apps import AppConfig
from django.db.models.signals import post_migrate

class SharedConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shared'
    
    def ready(self):
        from notes.models import create_default_notebook
        post_migrate.connect(create_default_notebook, sender=self)
