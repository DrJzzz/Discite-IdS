from rest_framework import serializers
from .models import Deck


class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = '__all__'
        
        
class DeckMaxReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck 
        fields = ['max_reviews']
        
    def update(self, instance, validated_data):
        instance.max_reviews = validated_data.get('max_reviews', instance.max_reviews)
        instance.save()
        return instance