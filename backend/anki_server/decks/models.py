from django.db import models
from django.contrib.postgres.fields import ArrayField
from userapp.models import get_default_user, CustomUser, create_default_user
from notes.models import Tag

class Deck(models.Model):
    id = models.AutoField(primary_key=True)

    tags = models.ManyToManyField('notes.Tag', blank=True)
    name = models.CharField(max_length=100)
    card_count = models.IntegerField(default=0)
    max_reviews = models.IntegerField(default=20)  
    owner = models.ForeignKey('userapp.CustomUser', 
                              related_name='deck_user',
                              on_delete=models.CASCADE,
                              default=create_default_user)
    
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    
    
def get_default_deck(sender, **kwargs):    
        deck, created = Deck.objects.get_or_create(
            name='Default Deck', 
            defaults=dict(owner=create_default_user)
        )
        return deck
    
    
def create_default_deck():    
        deck, created = Deck.objects.get_or_create(
            name='Default Deck', 
            defaults=dict(owner=get_default_user)
        )
        return deck