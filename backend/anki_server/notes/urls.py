from django.urls import include, path
from rest_framework import routers, viewsets
from notes.views import *


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

router = routers.DefaultRouter()
router.register(r'notes', NoteViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('allnotes/', NoteList.as_view()),  # /notes/allnotes
    #path('note/<int>', NoteDetail.as_view())
]
