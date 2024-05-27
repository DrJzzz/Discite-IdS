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
        
    def create(self, validated_data):
     
        sharer = validated_data['sharer']
        recipient = validated_data['recipient']
        
        deck_shared = validated_data['deck_shared']
        notebook_shared = validated_data['notebook_shared']
        
        deck = validated_data['deck']
        notebook = validated_data['notebook']

        obj = 'deck'
        
        print(sharer, recipient, deck_shared, notebook_shared, deck, notebook)
        
        if  deck_shared and notebook_shared :
            raise ValidationError(_("Cannot shared both deck and notebook")).as_json()
            
        
        elif deck_shared:
            list = Shared.objects.filter(sharer=sharer, recipient=recipient, deck=deck)
           
        
        elif notebook_shared:
            obj = 'notebook'
            list = Shared.objects.filter(sharer=sharer, recipient=recipient, notebook=notebook)
            
        if len(list) == 0:
            shared = serializer.save()
            return response.Response(serializer.data)
        
        
        else:
            values = []
            for x in list :
                json  = model_to_dict(x)
                values.append(json)
                
            data = {'message': 'already shared',
                    'data' : values 
                    }
            raise  ValidationError(_("Invalid value: %(message)s, \n %(data)s"),
                                    code="invalid",
                                    params=data,
                                    )

        
    
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)