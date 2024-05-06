from rest_framework import serializers
from notes.models import Note, Tag, Notebook



class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        # fields =['title', 'content', 'id', 'owner']
        fields = '__all__'
        

class TagSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Tag
        fields = '__all__'
        
class NotebookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notebook
        fields = '__all__'