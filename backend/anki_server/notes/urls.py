from django.urls import include, path
from rest_framework import routers, viewsets
from notes.views import *



router = routers.DefaultRouter()
router.register(r'notes', NoteViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('allnotes/', NoteList.as_view()),  # /notes/allnotes
    #path('note/<int:pk>/', NoteDetail.as_view())
]
