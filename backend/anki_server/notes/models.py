from django.db import  models
from userapp.models import CustomUser, create_default_user, get_default_user




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
    # linkedTo =  models.ManyToManyField("self", blank=True)
    # linkedFrom = models.ManyToManyField("self", blank=True)
    

    def __str__(self):
        return self.title
    
    
    
class Notebook(models.Model):
    name = models.CharField(max_length=255)
    notes = models.ManyToManyField('Note', blank=True, null=True)
    tags = models.ManyToManyField('Tag', blank=True, null=True)
    owner = models.ForeignKey('userapp.CustomUser', 
                              related_name='note_user',
                              on_delete=models.CASCADE,
                              default=create_default_user)