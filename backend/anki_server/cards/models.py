

from django.contrib.postgres.fields import ArrayField
from django.db import models

class Card(models.Model):
    id = models.AutoField(primary_key=True)
    lastAnswer = models.IntegerField(blank=True, null=True)
    lastStudied = models.IntegerField(blank=True, null=True)
    ease = models.FloatField(blank=True, null=True)
    interval = models.TimeField(blank=True, null=True)
    due = models.DateTimeField(blank=True, null=True)
    reviews = models.IntegerField(blank=True, null=True)
    lapses = models.IntegerField(blank=True, null=True)
    avgTime = models.TimeField(blank=True, null=True)
    tags = ArrayField(models.CharField(max_length=100), blank=True,null=True)
    modified = models.DateTimeField(blank=True, null=True)
    subject = models.CharField(max_length=100, blank=True, null=True)
    data = models.JSONField(blank=True, null=True)
    deck = models.ForeignKey('decks.Deck', related_name='card_deck',on_delete=models.CASCADE)

    def __str__(self):
        return self.id



