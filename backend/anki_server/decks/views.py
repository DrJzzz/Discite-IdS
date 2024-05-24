from django.shortcuts import render
from rest_framework import generics, response, views, viewsets
from .models import Deck
from .serializers import DeckSerializer, DeckMaxReviewSerializer
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers  import FormParser
from rest_framework.decorators import action
from rest_framework import serializers, status


from datetime import datetime
from django.utils.timezone import make_aware 

class DeckList(generics.ListCreateAPIView):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer

class DeckDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer




class DeckViewSet(viewsets.ModelViewSet):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    permission_classes = [IsAuthenticated]
    
    @action(detail=True, serializer_class=DeckMaxReviewSerializer, methods=['PATCH'])
    def update_review(self, request, *args, **kwargs):
        deck = self.get_object()
        new_max_reviews = request.data.get('max_reviews', 5)#data['max_reviews']
        deck.max_reviews = new_max_reviews
        deck.save()
        
        serializer = DeckSerializer(instance=deck)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['GET'])
    def cards(self, request, *args, **kwargs):
        deck = self.get_object()
        cards = deck.card_deck.all()

        data = {
            'deck': {
                'id': deck.id,
                'name': deck.name,
                'public': deck.public
            },
            'cards': list(cards.values('id', 'front'))
        }
        return JsonResponse(data)

    
    @action(detail=True, methods=['GET'])
    def to_review(self, request, *args, **kwargs):
        user = request.user
        decks = Deck.objects.filter(owner=user.id)
        
        values = []
        for deck in decks:
            cards = deck.card_deck.filter(due__lte=make_aware(datetime.today()))
            value = {
                'count' : len(cards),
                'deck' : deck.id,
                'cards' : list(cards.values('id'))
            }
            values.append(value)
            
            
        data = {
            'user': user.id,
            'values': list(values),
        }
        return JsonResponse(data)
        
        
    @action(detail=True)
    def set_public(self, request, *args, **kwargs):
        deck = self.get_object()
        
        if not deck.public :
            deck.public = True
            deck.save()
            
        serializer = DeckSerializer(deck, context={'request': request})
        return Response(serializer.data, status=200)

    @action(detail=True)
    def set_private(self, request, *args, **kwargs):
        deck = self.get_object()
        
        if deck.public :
            deck.public = False
            deck.save()
            
        serializer = DeckSerializer(deck, context={'request': request})
        return Response(serializer.data, status=200)