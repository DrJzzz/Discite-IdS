from django.db import models
from mdeditor.fields import MDTextField


class Note(models.Model):
    title : models.CharField(max_length=255)
    content : models.TextField()
    tags : models.ManyToManyField(Tag)
    lastEdited : models.DateTimeField()
    dateCreated : models.DateTimeField()
    linkedTo :  models.ManyToManyField(Note)
    linkedFrom : models.MayToManyField(Note)

class Tag(models.Model):
    name : models.CharField()
