from django.urls import include, path

from notes.views import *

urlpatterns = [
    path('allnotes/', NoteList.as_view()),  # /notes/allnotes
    path('note/<int>', NoteDetail.as_view())
]
