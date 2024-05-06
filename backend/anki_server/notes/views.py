from django.shortcuts import render

from rest_framework import generics, viewsets
from notes.models import *
from notes.serializers import *
from .models import Notebook
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from rest_framework.permissions import (AllowAny, IsAuthenticated)
from rest_framework.response import Response



class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NotebookViewSet(viewsets.ModelViewSet):
    queryset = Notebook.objects.all()
    serializer_class = NotebookSerializer

    # def create(self, request, *args, **kwargs):
    #     user = request.user
    #     data = request.data
    #     response = super(NotebookViewSet, self).create(request, *args, **kwargs)
    #     serializer = NotebookOwnerSerializer(instance=response.data, data=user)
    #     return response
    #def perform_create(self, serializer):
     #   serializer.save(owner=self.request.user)


def notes_notebook(request, pk):
    notebook = get_object_or_404(Notebook, pk=pk)
    notes = notebook.notebook_ref.all()

    data = {
        'notebook': {
            'id': notebook.id,
            'name': notebook.name,
        },
        'notes': list(notes.values('id'))
    }

    return JsonResponse(data)