from django.urls import path,include, re_path
from rest_framework import routers
from .views import CardList, CardDetail, FlashCardViewSet, CardViewSet


router = routers.DefaultRouter()
router.register(r'cards', CardViewSet, basename='card' )
router.register(r'fcards', FlashCardViewSet, basename='flashcard')


urlpatterns = [
    path('', include(router.urls)),
]