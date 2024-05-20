from rest_framework import serializers
from .models import Card, FlashCard, State

class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

        
        
        
class FlashCardSerializer( serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FlashCard
        fields = ["id", "due", "stability", "difficulty", "elapsed_days",
                  "scheduled_days", "reps", "lapses", "state", "last_review",
                  "template", "front", "back", "deck", "tags"]
        
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)        
        
 