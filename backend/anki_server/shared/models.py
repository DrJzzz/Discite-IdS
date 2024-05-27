from django.db import models
from userapp.models import get_default_user, CustomUser, create_default_user
from decks.models import *
from notes.models import *

class Shared(models.Model):
    #id = models.AutoField(primary_key=True)
    sharer = models.ForeignKey('userapp.CustomUser', 
                              related_name='sharer',
                              on_delete=models.CASCADE,
                              default=create_default_user)
    recipient = models.ForeignKey('userapp.CustomUser', 
                              related_name='recipient',
                              on_delete=models.CASCADE,
                              default=create_default_user)
    deck_shared = models.BooleanField(default=False)
    notebook_shared = models.BooleanField(default=False)
    
    deck = models.ForeignKey('decks.Deck', 
                              related_name='shared_deck',
                              on_delete=models.CASCADE,
                              default=create_default_deck)
    notebook = models.ForeignKey('notes.Notebook', 
                              related_name='shared_notebook',
                              on_delete=models.CASCADE,
                              default=get_default_notebook)
    
