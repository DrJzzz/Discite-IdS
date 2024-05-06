from django.urls import path,include, re_path
from rest_framework import routers
from .views import CardList, CardDetail, FlashCardViewSet, CardViewSet


router = routers.DefaultRouter()
router.register(r'cards', CardViewSet, basename='card' )
router.register(r'fcards', FlashCardViewSet, basename='flashcard')


urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^cards/(?P<pk>\d+)/set_new_rating/(?P<rating>\d+)/$', CardViewSet.set_new_rating),
]