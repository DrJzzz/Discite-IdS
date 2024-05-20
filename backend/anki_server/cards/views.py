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

    

    @action(detail=True, methods=['POST'])
    def set_new_rating(self, request, pk):
        # get data from route
        card = self.get_object()
        rating = int(request.data['rating'])
        # print("Before offset : %s", str(datetime.now()))
        timezone_offset = -60.0
        tzinfo = timezone(-timedelta(hours=6))
        
        # print("After offset : %s", str(datetime.now(tzinfo)))
        
        # timedelta(hours=timezone_offset)
        fsrs_scheduling_cards = FSRS().repeat(card, datetime.now(tzinfo))
        card = fsrs_scheduling_cards[rating].card
        # print(str(card.due))
        card.save()

        return Response({'new_rating': request.data['rating']})
    
    @action(detail=True, methods=['GET'])
    def get_history(self, request, *args, **kwargs):
        card = self.get_object()
        serializer = FlashcardHistorySerializer(card, context={'request': request})
        return response.Response(serializer.data, status=status.HTTP_200_OK)
    
    
    

    
    
