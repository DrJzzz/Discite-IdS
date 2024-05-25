from rest_framework import serializers
from shared.models import *


class SharedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shared
        fields = '__all__'