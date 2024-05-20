from rest_framework import serializers
from notes.models import Note, Tag, Notebook
from simple_history.models import HistoricalRecords


class NoteHistoryField(serializers.ListField):
    child = serializers.DictField()
    
    def to_representation(self, data):
        return super().to_representation(data.values())

class NoteHistorySerializer(serializers.HyperlinkedModelSerializer):
    history = NoteHistoryField(read_only=True)
    class Meta:
        model = Note
        fields = ['history']


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'dateCreated', 'notebook_ref', 'tags']
        
        
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