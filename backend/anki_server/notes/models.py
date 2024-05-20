from django.db import  models
from userapp.models import CustomUser, create_default_user, get_default_user

# for change history tracking
from simple_history.models import HistoricalRecords


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
    notebook_ref = models.ForeignKey('notes.Notebook', 
                                     related_name='notebook_ref', 
                                     on_delete=models.CASCADE)
    history = HistoricalRecords()

    def __str__(self):
        return self.title
    
    
    
class Notebook(models.Model):
    name = models.CharField(max_length=255)
    notes = models.ManyToManyField('Note', blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    owner = models.ForeignKey('userapp.CustomUser', 
                              related_name='note_user',
                              on_delete=models.CASCADE,
                              default=create_default_user)
    
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