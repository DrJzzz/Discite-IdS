from rest_framework import serializers
from .models import Card, FlashCard, State

# class CardSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Card
#         fields = '__all__'
        
class FlashCardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FlashCard
        fields = ['front', 'back']
        
