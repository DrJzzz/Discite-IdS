from django.shortcuts import render

from rest_framework import generics, viewsets, response, status 
from notes.models import *
from notes.serializers import *
from .models import Notebook
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from rest_framework.permissions import (AllowAny, IsAuthenticated)
from rest_framework.response import Response

from rest_framework.decorators import action
from rest_framework.response import Response

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    
    @action(detail=True, methods=['GET'])
    def get_history(self, request, *args, **kwargs):
        note = self.get_object()
        serializer = NoteHistorySerializer(note, context={'request': request})
        return response.Response(serializer.data, status=status.HTTP_200_OK)
    
    # @action(detail=True, methods=['GET'])
    # def get_last_edited(self, request, *args, **kwargs):
    #     history = self.get_object().history.order_by('history_date')[:1].get()
    #     serializer = HistoricalRecordsSerializer(history)
    #     return response.Response(serializer.data, status=status.HTTP_200_OK)
    
    # @action(detail=True, methods=['GET'])
    # def get_created(self, request, *args, **kwargs):
    #     history = self.get_object().history.filter(comment='Created')
    #     serializer = NoteHistoru
    #     return response.Response(history, status=status.HTTP_200_OK)

class NotebookViewSet(viewsets.ModelViewSet):
    queryset = Notebook.objects.all()
    serializer_class = NotebookSerializer    
    
    def perform_create(self, serializer):
       serializer.save(owner=self.request.user)






def notes_notebook(request, pk):
    notebook = get_object_or_404(Notebook, pk=pk)
    notes = notebook.notebook_ref.all()

    data = {
        'notebook': {
            'id': notebook.id,
            'name': notebook.name,
        },
        'notes': list(notes.values('id', 'title'))
    }

    return JsonResponse(data)