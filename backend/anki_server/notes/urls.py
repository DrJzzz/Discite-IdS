from django.urls import include, path
from rest_framework import routers, viewsets
from notes.views import *



router = routers.DefaultRouter()
router.register(r'notes', NoteViewSet)
router.register(r'notebooks', NotebookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
