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
    
    
    
        
        
    
