from django.db import  models
from userapp.models import CustomUser, create_default_user, get_default_user

# for change history tracking
from simple_history.models import HistoricalRecords


from django.db.models.signals import pre_delete
from django.dispatch import receiver

def get_default_note(sender, **kwargs):
    notebook, created = Notebook.objects.get_or_create(
        name='Default Notebook',
        defaults=dict(owner=create_default_user)
    )
    return notebook


def create_default_note():
    notebook, created = Notebook.objects.get_or_create(
        name='Default Notebook',
        defaults=dict(owner=get_default_user)
    )
    return notebook

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Note(models.Model):   
    title = models.CharField( max_length=255)
    content = models.TextField()
    tags = models.ManyToManyField("Tag", blank=True)
    dateCreated = models.DateTimeField(auto_now_add=True, blank=True)
    notebook = models.ForeignKey('notes.Notebook', 
                                related_name='notebook', 
                                on_delete=models.CASCADE)
    history = HistoricalRecords()
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.title 
    
    
    
class Notebook(models.Model):
    name = models.CharField(max_length=255)
    tags = models.ManyToManyField('Tag', blank=True)
    owner = models.ForeignKey('userapp.CustomUser', 
                              related_name='note_user',
                              on_delete=models.CASCADE,
                              default=create_default_user)
    note_count = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

def create_default_notebook(sender, **kwargs):    
        notebook, created = Notebook.objects.get_or_create(
            name='Default Notebook', 
            defaults=dict(owner=create_default_user)
        )
        return notebook
    
def get_default_notebook():    
        notebook, created = Notebook.objects.get_or_create(
            name='Default Notebook', 
            defaults=dict(owner=get_default_user)
        )
        return notebook
    
    

@receiver(pre_delete, sender=Note)
def decrement_deck_count(sender, instance, using, **kwargs):  
    instance.notebook.note_count = instance.notebook.note_count - 1
    instance.notebook.save()
