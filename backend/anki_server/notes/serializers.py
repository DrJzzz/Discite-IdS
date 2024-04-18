from rest_framework import serializers
from notes.models import Note, Tag


class NoteHyperLinkedRelatedField(serializers.HyperlinkedRelatedField):
    lookup_field = 'id'

class NoteSerializer(serializers.HyperlinkedModelSerializer):
    serializer_related_field = NoteHyperLinkedRelatedField
    
    class Meta:
        model = Note
        fields = ['url', 'id','title', 'content']
        # extra_kwargs = {
        #     "url": {"lookup_url_kwarg": "id"},
        # }
        



class TagSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Tag
        fields = '__all__'