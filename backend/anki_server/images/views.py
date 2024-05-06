from django.shortcuts import render
from rest_framework import permissions, viewsets, generics
from images.serializers import ImageSerializer
from images.models import Image

from rest_framework.parsers import (MultiPartParser, FormParser)
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.permissions import (AllowAny, IsAuthenticated)

class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
    permission_classes = [IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        user = request.user 
        response = super(ImageViewSet, self).create(request, *args, **kwargs)
        response.data = {'id-url': response.data['image']}
        return response
    
