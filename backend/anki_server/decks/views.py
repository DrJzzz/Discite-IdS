from django.shortcuts import render
from rest_framework import generics
from .models import Deck
from .serializers import DeckSerializer
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


class DeckList(generics.ListCreateAPIView):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer

class DeckDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer

def cards_deck(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    cards = deck.card_deck.all()

    data = {
        'deck': {
            'id': deck.id,
            'name': deck.name,
            'cards_count': deck.cards_count,
            'max_reviews' : deck.max_reviews,
            'due_today' : deck.due_today
        },
        'cards': list(cards.values('id','lastAnswer', 'lastStudied', 'ease',
                                   'interval', 'due', 'reviews', 'lapses',
                                   'avgTime', 'tags', 'modified', 'subject',
                                   'data')),
    }
    return JsonResponse(data)
