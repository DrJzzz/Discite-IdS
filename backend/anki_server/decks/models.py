from django.db import models
from django.contrib.postgres.fields import ArrayField



# Create your models here.
class Deck(models.Model):
    id = models.AutoField(primary_key=True)

    tags = ArrayField(models.CharField(max_length=100), blank=True, null=True)
    name = models.CharField(max_length=100)
    cards_count = models.IntegerField(default=0)
    max_reviews = models.IntegerField(default=0)
    due_today = models.IntegerField(default=0)
    #owner = models.ForeignKey('userapp.CustomUser', related_name='deck_user',on_delete=models.CASCADE)


    def __str__(self):
        return self.name


def create_deck():
    print("hello")
    # if not Deck.objects.exists():
    #     Deck.objects.create(name="Global", owner=1)