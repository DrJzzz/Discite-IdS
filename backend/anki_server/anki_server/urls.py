from django.contrib import admin
from django.urls import include, path, re_path

from django.contrib.auth import get_user_model
from rest_framework import routers, serializers, viewsets

from userapp import views as userviews
from notes import views as noteviews
from userapp.models import CustomUser


router = routers.DefaultRouter()
router.register(r'users', userviews.UserViewSet)
router.register(r'groups', userviews.GroupViewSet)
router.register(r'notes', noteviews.NoteViewSet)




urlpatterns = [
    path('', include('userapp.urls')),
    path('', include('cards.urls')),
    path('', include('decks.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    re_path(r'^rest-auth/', include('exarth_rest_auth.urls')),
    re_path(r'^rest-auth/registration/', include('exarth_rest_auth.registration.urls')),
    re_path(r'^rest-auth/', include('exarth_rest_auth.urls')),
    path('notes/', include('notes.urls'))
]
