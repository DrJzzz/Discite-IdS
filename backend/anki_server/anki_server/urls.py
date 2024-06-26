from django.contrib import admin
from django.urls import include, path, re_path

from django.contrib.auth import get_user_model
from rest_framework import routers, serializers, viewsets

from userapp import views as userviews
from notes.views import NoteViewSet, NotebookViewSet, TagViewSet
from cards.views import FlashCardViewSet
from images.views import ImageViewSet
from django.conf.urls.static import static
from anki_server import settings
from decks.views import DeckViewSet
from shared.views import SharedViewSet

router = routers.DefaultRouter()
router.register(r'users', userviews.UserViewSet)
router.register(r'groups', userviews.GroupViewSet)
router.register(r'notes', NoteViewSet)
router.register(r'fcards', FlashCardViewSet)
router.register(r'img', ImageViewSet)
router.register(r'notebooks', NotebookViewSet)
router.register(r'decks', DeckViewSet)
router.register(r'shared', SharedViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = [
    path('', include('userapp.urls')),
    path('', include('cards.urls')),
    path('', include('decks.urls')),
    path('', include('notes.urls')),
    path('', include('images.urls')),
    path('', include('shared.urls')),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    re_path(r'^rest-auth/', include('exarth_rest_auth.urls')),
    re_path(r'^rest-auth/registration/', include('exarth_rest_auth.registration.urls')),
    re_path(r'^rest-auth/', include('exarth_rest_auth.urls')),
   #  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
