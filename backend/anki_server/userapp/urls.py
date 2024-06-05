from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .views import *


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('users/<int:pk>/decks/', decks_user, name='decks-user'),
    path('users/<int:pk>/notebooks/', notebooks_user, name='notebooks-user'),
]

