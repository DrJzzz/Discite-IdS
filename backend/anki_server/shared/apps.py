from django.apps import AppConfig


class SharedConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shared'
    
    def ready(self):
        from notes.models import create_default_notebook
        post_migrate.connect(create_default_notebook, sender=self)
