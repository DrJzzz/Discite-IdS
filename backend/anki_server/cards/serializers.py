from rest_framework import serializers
from .models import Card, FlashCard, State


class CardHistoryField(serializers.ListField):
    child = serializers.DictField()
    
    def to_representation(self, data):
        return super().to_representation(data.values())

class FlashcardHistorySerializer(serializers.HyperlinkedModelSerializer):
    history = CardHistoryField(read_only=True)
    class Meta:
        model = FlashCard
        fields = ['history']
        


class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'
        abstract = True
        
        
        
class FlashCardSerializer( serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FlashCard
        fields = '__all__'
        
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)        
        
 
