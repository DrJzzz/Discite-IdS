from django.urls import include, path
from rest_framework import routers, viewsets
from .views import *



router = routers.DefaultRouter()
router.register(r'notes', NoteViewSet)
router.register(r'notebooks', NotebookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('notebooks/<int:pk>/notes/', notes_notebook,name='notes-notebook'),
]
