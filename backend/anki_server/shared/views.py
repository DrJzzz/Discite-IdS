from django.shortcuts import render
from shared.models import *
from shared.serializers import *
from rest_framework import routers, serializers, viewsets, response, status
from django.http import JsonResponse
from rest_framework.decorators import action



class SharedViewSet(viewsets.ModelViewSet):
    queryset = Shared.objects.all().order_by('id')
    serializer_class = SharedSerializer
    
    @action(detail=False, methods=['GET'])
    def shared_with_me(self, request, *args, **kwargs):
        user = request.user
        shared_with_me = Shared.objects.filter(recipient=user.id)
        
        values = []
        type = 0 
        id = 0
        for item in shared_with_me:
            if (item.deck_shared): 
                type = 1
                id = item.deck.id
            else:
                type = 2
                id = item.notebook.id
                
                
            value = {
                'type' : type, 
                'id'  : id,
                'user' : item.sharer.id
            }
            values.append(value)
        
        data = {
            'count' : len(values),
            'values' : list(values)
        }
        
        return JsonResponse(data, safe=False)
        
    @action(detail=False, methods=['GET'])
    def shared_with(self, request, *args, **kwargs):
        user = request.data.get('user')
        
        try:
            deck = request.data.get('deck')
        except:
            deck = None
        try:            
            notebook = request.data.get('notebook')
        except:
            notebook = None
        
        list = []

        if deck is not None:
            list = Shared.objects.filter(sharer=user, deck=deck)
        
        if notebook is not None:
            list = Shared.objects.filter(sharer=user, notebook=notebook)
            
            
            
        values = []
        
        for x in list:
            user = x.recipient
            #user = CustomUser.objects.filter(id=recipient)
            item = {
                'id' : user.id,
                'name' : user.name,
                'email' : user.email
            }
            values.append(item)
            
        return response.Response(data=values)
    
    
    def perform_create(self, serializer):
     
        sharer = serializer.validated_data['sharer']
        recipient = serializer.validated_data['recipient']
        
        try:
            deck_shared = serializer.validated_data['deck_shared']
        except:
            deck_shared = False      
       
        try:
            notebook_shared = serializer.validated_data['notebook_shared']
        except:
            notebook_shared = False      
       

        obj = 'deck'
        
        
        if  deck_shared and notebook_shared :
            raise ValidationError(_("Cannot shared both deck and notebook")).as_json()
            
        
        elif deck_shared:
            deck = serializer.validated_data['deck']
            list = Shared.objects.filter(sharer=sharer, recipient=recipient, deck=deck)
           
        
        elif notebook_shared:
            notebook = serializer.validated_data['notebook']
            obj = 'notebook'
            list = Shared.objects.filter(sharer=sharer, recipient=recipient, notebook=notebook)
            
        if len(list) == 0:
            serializer.is_valid(raise_exception=True)
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
    
    
    
        
        
    
