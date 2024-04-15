from django.db import models

class Note(models.Model):
    title : models.CharField(max_length=255)
    content : models.TextField()
    tags : models.ManyToManyField(Tag)
    lastEdited : models.DateTimeField()
    dateCreated : models.DateTimeField()
    linkedTo :  models.ManyToManyField(Note)
    linkedFrom : models.MayToManyField(Note)

    def __str__(self):
        return self.title

class Tag(models.Model):
    name : models.CharField()

    def __str__(self):
        return self.name
