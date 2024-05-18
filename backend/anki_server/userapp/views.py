
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from userapp.serializers import GroupSerializer, UserSerializer, SimpleUserSerializer
from .models import CustomUser
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


from rest_framework.views import APIView
from rest_framework.response import Response
import jwt, datetime


from django.http import JsonResponse
from rest_framework.decorators import action

class RegisterView(APIView):
    def post(self, request):
        serializer  = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)





class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
    @action(detail=False, methods=['GET'])
    def list_all(self, request, *args, **kwargs):
        users = CustomUser.objects.all()
        values = []
        for user in users:
            item = {
                'id' : user.id,
                'name' : user.name,
                'email' : user.email
            }
            values.append(item)

        data = {
            'count' : len(values),
            'users' : list(values)
        }
        
        return JsonResponse(data, safe=False)

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    #permission_classes = [permissions.IsAuthenticated]

    



def decks_user(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    decks = user.deck_user.all()

    data = {
        'user': user.id,
        'decks': list(decks.values('id', 'name')),
    }
    return JsonResponse(data)


def notebooks_user(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    notebooks = user.note_user.all()

    data = {
        'user': user.id,
        'notebooks': list(notebooks.values('id', 'name')),
    }
    return JsonResponse(data)

