from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .views import *

router = routers.DefaultRouter()
router.register(r'shared', SharedViewSet)

urlpatterns = [
    path('', include(router.urls)),
]