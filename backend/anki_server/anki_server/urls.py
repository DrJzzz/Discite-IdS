"""
URL configuration for anki_server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from django.contrib.auth import get_user_model
from rest_framework import routers, serializers, viewsets
from snippets.models import CustomUser


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email','name', 'birthdate', 'max_reviews', 'phone_number']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('snippets.urls')),
    path('accounts/', include('allauth.urls')),
    re_path(r'^rest-auth/', include('exarth_rest_auth.urls')),
    re_path(r'^rest-auth/registration/', include('exarth_rest_auth.registration.urls')),
    re_path(r'^rest-auth/', include('exarth_rest_auth.urls'))
]

urlpatterns += router.urls