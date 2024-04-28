from django.contrib.postgres.fields import ArrayField
from django.db import models
from notes.models import Tag
from datetime import datetime
from typing import Optional
from decks.models import *


class State(models.IntegerChoices):
    New = 0
    Learning = 1
    Review = 2
    Relearning = 3

class Card(models.Model):

    class Template(models.IntegerChoices):
        FLASHCARD = 1
 

    id = models.AutoField(primary_key=True)

    # Metadata
    due = models.DateTimeField(auto_now_add=True, null=True)
    stability = models.FloatField(default=0)
    difficulty = models.FloatField(default=0)
    elapsed_days = models.IntegerField(default=0)
    scheduled_days = models.IntegerField(default=0)
    reps = models.IntegerField(default=0)
    lapses = models.IntegerField(default=0)
    state = models.IntegerField(choices=State, default=0)
    last_review = models.DateTimeField(blank=True, null=True)

    # Relations    
    tags = models.ManyToManyField("notes.Tag", blank=True)
    deck = models.ForeignKey('decks.Deck', 
                             related_name='card_deck',
                             on_delete=models.CASCADE,
                             default=get_default_deck)
    
    template = models.IntegerField(choices=Template, 
                                   default=1)    

    def __str__(self):
        return self.id


    def __deepcopy__(self, memo):
        cls = self.__class__
        newobject = cls.__new__(cls)
        newobject.__dict__.update(self.__dict__)
        return newobject

    def __init__(self) -> None:
        self.due = datetime.now
        self.stability = 0
        self.difficulty = 0
        self.elapsed_days = 0
        self.scheduled_days = 0
        self.reps = 0
        self.lapses = 0
        self.state = State.New


    def get_retrievability(self, now: datetime) -> Optional[float]:
        DECAY = -0.5
        FACTOR = 0.9 ** (1 / DECAY) - 1

        if self.state == State.Review:
            elapsed_days = max(0, (now - self.last_review).days)
            return (1 + FACTOR * elapsed_days / self.stability) ** DECAY
        else:
            return None





class FlashCard(Card):
    front = models.TextField(blank=True)
    back = models.TextField(blank=True)


