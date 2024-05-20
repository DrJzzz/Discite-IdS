from rest_framework import serializers
from notes.models import Note, Tag, Notebook



class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        # fields =['title', 'content', 'id', 'owner']
        fields = ['id', 'title', 'content', 'lastEdited', 'dateCreated', 'notebook_ref', 'tags']
        

class TagSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Tag
        fields = '__all__'
        
class NotebookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notebook
        fields = ['name', 'notes', 'tags']
        
        
class NotebookOwnerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notebook
        fields = 'owner'
        
    def update(self, instance, validated_data):
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance