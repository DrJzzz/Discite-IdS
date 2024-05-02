from django.urls import path,include
from rest_framework import routers
from .views import CardList, CardDetail, FlashCardViewSet, CardViewSet


router = routers.DefaultRouter()
router.register(r'cards', CardViewSet, basename='card' )
router.register(r'fcards', FlashCardViewSet, basename='flashcard' )
#router.register(r'cards/(?P<id>[-\w]+)', CardViewSet, basename='card')

urlpatterns = [
    path('', include(router.urls)),
    #path('cards/', CardList.as_view(), name='card-list'),
    #path('cards/<int:pk>/', CardDetail.as_view(), name='card-detail'),
]