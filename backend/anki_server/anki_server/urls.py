from django.contrib import admin
from django.urls import include, path, re_path

from django.contrib.auth import get_user_model
from rest_framework import routers, serializers, viewsets

from userapp import views
from notes import views as noteviews


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'notes', noteviews.NoteViewSet)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('notes/', include('notes.urls'))
]
