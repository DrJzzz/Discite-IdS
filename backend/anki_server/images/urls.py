from django.urls import path,include
from rest_framework import routers
from images.views import ImageViewSet


router = routers.DefaultRouter()
router.register(r'img', ImageViewSet, basename='img' )


urlpatterns = [
    path('', include(router.urls)),
]