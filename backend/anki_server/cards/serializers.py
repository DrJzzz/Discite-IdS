from rest_framework import serializers
from .models import Card

class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'lastAnswer', 'lastStudied', 'ease', 'interval', 'due', 'reviews', 'lapses', 'avgTime',
                  'tags', 'modified', 'subject','data', 'deck']
