from django.shortcuts import render
from rest_framework import generics, viewsets, mixins, response, status
from .models import Card, FlashCard
from .serializers import  FlashCardSerializer
from datetime import datetime


class CardList(generics.ListCreateAPIView):
    queryset = FlashCard.objects.all()
    serializer_class = FlashCardSerializer

class CardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FlashCard.objects.filter()
    serializer_class = FlashCardSerializer



    
class FlashCardViewSet(viewsets.ModelViewSet):
    queryset = FlashCard.objects.all()
    serializer_class = FlashCardSerializer
    
    # def retrieve(self, request, pk=None):
    #     u = request.user
    #     queryset = Card.objects.filter(id=pk)
    #     if not queryset:
    #         return Response(status=status)
    
    
class CardViewSet(viewsets.ModelViewSet, mixins.CreateModelMixin):
    # queryset = Card.objects.all()
    # serializer_class = CardSerializer
    def get_queryset(self):
        return Card.objects.all().order_by('id')
    
    def create(self, request, *args, **kwargs):
        card_serializer = Card.get_serializer()
        serializer = card_serializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get_serializer_class(self):
        return Card.get_serializer()
    
    
def to_review(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    decks = user.deck_user.all()
    values = []
    for deck in decks:
        cards = deck.card_deck.filter(due__lt=datetime.today())
        value = {
            'deck' : deck.id,
            'cards' : list(cards.values('id'))
        }
        values.append(values)
        
        
    data = {
        'user': user.id,
        'values': list(values),
    }
    return JsonResponse(data)
