from rest_framework import  serializers, response, status
from rest_framework.response import  Response
from shared.models import *
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.forms.models import model_to_dict




class SharedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shared
        fields = '__all__'
        
    