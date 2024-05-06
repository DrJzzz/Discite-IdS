from django.shortcuts import render

from rest_framework import generics, viewsets
from notes.models import *
from notes.serializers import *
from rest_framework.permissions import (AllowAny, IsAuthenticated)
from rest_framework.response import Response


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NotebookViewSet(viewsets.ModelViewSet):
    queryset = Notebook.objects.all()
    serializer_class = NotebookSerializer
    permission_classes = [IsAuthenticated]
    
    # def create(self, request, *args, **kwargs):
    #     user = request.user 
    #     data = request.data
    #     response = super(NotebookViewSet, self).create(request, *args, **kwargs)
    #     serializer = NotebookOwnerSerializer(instance=response.data, data=user)
    #     return response
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)       

        