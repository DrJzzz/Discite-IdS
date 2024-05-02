from django.db import  models
from userapp.models import get_default_user

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
    linkedTo =  models.ManyToManyField("self", blank=True)
    linkedFrom = models.ManyToManyField("self", blank=True)
    owner = models.ForeignKey('userapp.CustomUser', 
                              related_name='note_user',
                              on_delete=models.CASCADE,
                              default=get_default_user)


    def __str__(self):
        return self.title
    
