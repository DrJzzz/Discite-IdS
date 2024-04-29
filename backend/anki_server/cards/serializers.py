from rest_framework import serializers
from .models import Card, FlashCard

class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'
        
class FlashCardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FlashCard
        fields = '__all__'
