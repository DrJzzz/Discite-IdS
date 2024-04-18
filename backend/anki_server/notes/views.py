from django.shortcuts import render

from rest_framework import generics, viewsets
from notes.models import *
from notes.serializers import *

from notes.models import Note, Tag


class NoteList(generics.ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteDetail(generics.RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_url_kwarg = "id"



class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer