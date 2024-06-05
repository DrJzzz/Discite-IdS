from django.urls import include, path
from rest_framework import routers, viewsets
from .views import *

get_last_edited = NoteViewSet.as_view({
    'get' : 'list'
})


router = routers.DefaultRouter()
router.register(r'notes', NoteViewSet)
router.register(r'notebooks', NotebookViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #path('notebooks/<int:pk>/notes/', notes_notebook,name='notes-notebook'),
]
