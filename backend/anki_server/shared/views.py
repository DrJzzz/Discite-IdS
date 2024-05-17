from django.shortcuts import render
from shared.models import *
from shared.serializers import *
from rest_framework import routers, serializers, viewsets

class SharedViewSet(viewsets.ModelViewSet):
    queryset = Shared.objects.all().order_by('id')
    serializer_class = SharedSerializer
