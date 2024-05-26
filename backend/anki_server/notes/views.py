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
    
    
    @action(detail=True, methods=['PUT'])
    def revert_to(self, request, *args, **kwargs):
        current = self.get_object()
        revert_to = current.history.filter(history_id=request.data['id']).get()
        new_current = revert_to.instance.save()
        serializer = NoteSerializer(new_current, context={'request': request})
        return response.Response(serializer.data)
    
    
    
    def perform_create(self, serializer):
        note = serializer.save()
        note.notebook.note_count = note.notebook.note_count + 1
        note.notebook.save()
        
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    
    

    
class NotebookViewSet(viewsets.ModelViewSet):
    queryset = Notebook.objects.all()
    serializer_class = NotebookSerializer    
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
        
    @action(detail=True)
    def set_public(self, request, *args, **kwargs):
        notebook = self.get_object()
        
        if not notebook.public :
            notebook.public = True
            notebook.save()
            
        serializer = NotebookSerializer(notebook, context={'request': request})
        return Response(serializer.data, status=200)

    @action(detail=True)
    def set_private(self, request, *args, **kwargs):
        notebook = self.get_object()
        
        if notebook.public :
            notebook.public = False
            notebook.save()
            
        serializer = NotebookSerializer(notebook, context={'request': request})
        return Response(serializer.data, status=200)
    
    
    
    

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    



def notes_notebook(request, pk):
    notebook = get_object_or_404(Notebook, pk=pk)
    notes = notebook.notebook.all()

    data = {
        'notebook': {
            'id': notebook.id,
            'name': notebook.name,
            'public' : notebook.public
        },
        'notes': list(notes.values('id', 'title'))
    }

    return JsonResponse(data)