from django.shortcuts import render

from rest_framework import generics, viewsets
from notes.models import *
from notes.serializers import *
from .models import Notebook
from django.shortcuts import get_object_or_404
from django.http import JsonResponse



class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NotebookViewSet(viewsets.ModelViewSet):
    queryset = Notebook.objects.all()
    serializer_class = NotebookSerializer


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