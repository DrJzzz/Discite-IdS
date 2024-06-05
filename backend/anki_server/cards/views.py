from django.shortcuts import render
from rest_framework import generics, viewsets, mixins, response, status
from .models import Card, FlashCard
from cards.serializers import  *
from datetime import datetime, timedelta, timezone


from cards.fsrs import *
from rest_framework.decorators import action
from rest_framework.response import Response

from django.utils.timezone import make_aware

from decks.models import Deck

class CardList(generics.ListCreateAPIView):
    queryset = FlashCard.objects.all()
    serializer_class = FlashCardSerializer

class CardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FlashCard.objects.filter()
    serializer_class = FlashCardSerializer



    
class FlashCardViewSet(viewsets.ModelViewSet):
    queryset = FlashCard.objects.all()
    serializer_class = FlashCardSerializer
    
    
    
    
class CardViewSet(viewsets.ModelViewSet):
    queryset = FlashCard.objects.all() 
    serializer_class = FlashCardSerializer
    
    def perform_create(self, serializer):
      
        card = serializer.save()
        card.deck.card_count = card.deck.card_count + 1
        card.deck.save()
        
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)

    
    # Sets a new rating for the card being studied 
    @action(detail=True, methods=['POST'])
    def set_new_rating(self, request, pk):
        # get data from route
        card = self.get_object()
        rating = int(request.data['rating'])
        
        timezone_offset = -60.0
        tzinfo = timezone(-timedelta(hours=6))
        
        
        fsrs_scheduling_cards = FSRS().repeat(card, datetime.now(tzinfo))
        card = fsrs_scheduling_cards[rating].card
        card.save()

        return Response({'new_rating': request.data['rating']})
    
    # Returns the change history of the card
    @action(detail=True, methods=['GET'])
    def get_history(self, request, *args, **kwargs):
        card = self.get_object()
        serializer = FlashcardHistorySerializer(card, context={'request': request})
        return response.Response(serializer.data, status=status.HTTP_200_OK)
    
    # Reverts to a certain state in the change history 
    @action(detail=True, methods=['PUT'])
    def revert_to(self, request, *args, **kwargs):
        current = self.get_object()
        revert_to = current.history.filter(history_id=request.data['id']).get()
        new_current = revert_to.instance.save()
        serializer = FlashCardSerializer(new_current, context={'request': request})
        return response.Response(serializer.data)
    
    
    

    
    
