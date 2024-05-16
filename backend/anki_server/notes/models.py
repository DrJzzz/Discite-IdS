from django.db import  models
from userapp.models import CustomUser, create_default_user, get_default_user


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
    lastEdited = models.DateTimeField(auto_now_add=True, blank=True)
    dateCreated = models.DateTimeField(auto_now_add=True, blank=True)
    notebook_ref = models.ForeignKey('notes.Notebook', related_name='notebook_ref', on_delete=models.CASCADE)
    # linkedTo =  models.ManyToManyField("self", blank=True)
    # linkedFrom = models.ManyToManyField("self", blank=True)
    
    # notebook = models.ForeignKey('notes.Notebook', 
    #                           related_name='note_notebook',
    #                           on_delete=models.CASCADE,
    #                           default=)

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

def create_default_notebook(sender, **kwargs):    
        deck, created = Notebook.objects.get_or_create(
            name='Default Notebook', 
            defaults=dict(owner=create_default_user)
        )
        return deck
    
def get_default_notebok():    
        deck, created = Notebook.objects.get_or_create(
            name='Default Notebook', 
            defaults=dict(owner=get_default_user)
        )
        return deck