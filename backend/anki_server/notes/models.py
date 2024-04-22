from django.db import  models

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Note(models.Model):   
    title = models.CharField( max_length=255)
    content = models.TextField()
    tags = models.ManyToManyField("Tag", blank=True)
    lastEdited = models.DateTimeField()
    dateCreated = models.DateTimeField()
    linkedTo =  models.ManyToManyField("self", blank=True)
    linkedFrom = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.title
    
