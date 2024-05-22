from django.urls import path,include
from rest_framework import routers
from images.views import ImageViewSet
from django.views.static import serve
from anki_server import settings


router = routers.DefaultRouter()
router.register(r'img', ImageViewSet, basename='img' )


urlpatterns = [
    path('', include(router.urls)),
]