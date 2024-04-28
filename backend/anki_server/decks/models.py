from django.db import models
from django.contrib.postgres.fields import ArrayField
from userapp.models import get_default_user, CustomUser, create_default_user



# Create your models here.
class Deck(models.Model):
    id = models.AutoField(primary_key=True)

    tags = ArrayField(models.CharField(max_length=100), blank=True, null=True)
    name = models.CharField(max_length=100)
    cards_count = models.IntegerField(default=0)
    max_reviews = models.IntegerField(default=0)
    due_today = models.IntegerField(default=0)
    owner = models.ForeignKey('userapp.CustomUser', 
                              related_name='deck_user',
                              on_delete=models.CASCADE,
                              default=get_default_user)

    def __str__(self):
        return self.name
    
    
    def create_default_deck():    
        deck, created = Deck.objects.get_or_create(
            name='Default Deck', 
            defaults=dict(owner=get_default_user)
        )
        return deck
    
    # def get_default_deck():
    #     return Deck.objects.get(name='Default Deck').id
    
    
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