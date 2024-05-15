from django.shortcuts import render
from rest_framework import generics, response, views, viewsets
from .models import Deck
from .serializers import DeckSerializer, DeckMaxReviewSerializer
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers  import FormParser
from rest_framework.decorators import action
from rest_framework import serializers, status

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
        },
        'cards': list(cards.values('id'))
    }
    return JsonResponse(data)


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
        

# class ChangeMaxReviewAPIView(views.APIView):
#     permission_classes = [IsAuthenticated]
#     parser_classes = [FormParser]
    
    
#     def post(self, request, format = None):
#         user = request.user
#         serializer