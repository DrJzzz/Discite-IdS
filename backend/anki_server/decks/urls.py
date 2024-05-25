from django.urls import path,include
from .views import DeckList,DeckDetail, DeckViewSet
from rest_framework import routers, viewsets

router = routers.DefaultRouter()
router.register(r'decks', DeckViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('decks/',DeckList.as_view(),name='deck-list'),
    # path('decks/<int:pk>/',DeckDetail.as_view(),name='deck-detail'),
    # path('decks/<int:pk>/cards/', cards_deck,name='cards-deck'),
]