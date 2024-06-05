from django.shortcuts import render
from rest_framework import permissions, viewsets, generics
from images.serializers import ImageSerializer
from images.models import Image

from rest_framework.parsers import (MultiPartParser, FormParser)
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import action

from rest_framework.permissions import (AllowAny, IsAuthenticated)

class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
    permission_classes = [IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        user = request.user 
        image = Image(image=request.data['image'], owner=user)
        image.save()
        serializer = ImageSerializer(image, context={'request': request})
        data = {'url': serializer.data['image']}
        return Response(data)
    

