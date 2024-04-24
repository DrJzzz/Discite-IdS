from django.urls import path,include
from .views import DeckList,DeckDetail,cards_deck

urlpatterns = [
    path('decks/',DeckList.as_view(),name='deck-list'),
    path('decks/<int:pk>/',DeckDetail.as_view(),name='deck-detail'),
    path('decks/<int:pk>/cards/', cards_deck,name='cards-deck'),
]