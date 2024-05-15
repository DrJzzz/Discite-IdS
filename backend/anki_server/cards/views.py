from django.shortcuts import render
from rest_framework import generics, viewsets, mixins, response, status
from .models import Card, FlashCard
from cards.serializers import  FlashCardSerializer, CardSerializer
from datetime import datetime, timedelta, timezone


from cards.fsrs import *
from rest_framework.decorators import action
from rest_framework.response import Response


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

    

    @action(detail=True, methods=['POST'])
    def set_new_rating(self, request, pk):
        # get data from route
        card = self.get_object()
        rating = int(request.data['rating'])

        timezone_offset = -6.0
        tzinfo = timezone(timedelta(hours=timezone_offset))
        
        fsrs_scheduling_cards = FSRS().repeat(card, datetime.now(tzinfo))
        card = fsrs_scheduling_cards[rating].card
        card.save()

        return Response({'status': 'new rating set'})
    
    
    

    
    
