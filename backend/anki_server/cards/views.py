from django.shortcuts import render
from rest_framework import generics, viewsets, mixins, response, status
from .models import Card, FlashCard
from cards.serializers import  FlashCardSerializer, CardSerializer
from datetime import datetime, timedelta, timezone


from cards.fsrs import *
from rest_framework.decorators import action
from rest_framework.response import Response



class CardList(generics.ListCreateAPIView):
    queryset = FlashCard.objects.all()
    serializer_class = FlashCardSerializer

class CardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FlashCard.objects.filter()
    serializer_class = FlashCardSerializer



    
class FlashCardViewSet(viewsets.ModelViewSet):
    queryset = FlashCard.objects.all()
    serializer_class = FlashCardSerializer
    
    
    
    
class CardViewSet(viewsets.ModelViewSet, mixins.CreateModelMixin):
    queryset = FlashCard.objects.all() 
    serializer_class = CardSerializer
    
    # def get_queryset(self):
    #     return FlashCard.objects.all().order_by('id')

    def create(self, request, *args, **kwargs):
        card_serializer = FlashCard.get_serializer()
        serializer = card_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_serializer_class(self):
        return FlashCard.get_serializer()

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
    
    # def to_review(request, pk):
    #     user = get_object_or_404(CustomUser, pk=pk)
    #     decks = user.deck_user.all()
    #     values = []
    #     for deck in decks:
    #         cards = deck.card_deck.filter(due__lt=datetime.today())
    #         value = {
    #             'deck' : deck.id,
    #             'cards' : list(cards.values('id'))
    #         }
    #         values.append(values)
            
            
    #     data = {
    #         'user': user.id,
    #         'values': list(values),
    #     }
    #     return JsonResponse(data)

    
    
