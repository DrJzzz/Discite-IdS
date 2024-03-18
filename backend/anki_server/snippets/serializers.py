from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES, CustomUser
from exarth_rest_auth.registration.serializers import RegisterSerializer
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from allauth.account.adapter import get_adapter
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'email','name', 'birthdate', 'max_reviews', 'phone_number',"snippets"]

class CustomRegisterSerializer(RegisterSerializer):
    name = serializers.CharField(max_length=100, required=True)
    birthdate = serializers.DateField(required=True)
    max_reviews = serializers.IntegerField(default=0)
    phone_number = serializers.CharField(max_length=10, required=True)

    def custom_signup(self, request, user):
        user.name = self.validated_data.get('name', '')
        user.birthdate = self.validated_data.get('birthdate', '')
        user.max_reviews = self.validated_data.get('max_reviews', 0)
        user.phone_number = self.validated_data.get('phone_number', '')
        user.save()

    def get_cleaned_data(self):
        cleaned_data = super().get_cleaned_data()
        cleaned_data.update({
            'name': self.validated_data.get('name', ''),
            'birthdate': self.validated_data.get('birthdate', ''),
            'max_reviews': self.validated_data.get('max_reviews', 0),
            'phone_number': self.validated_data.get('phone_number', '')
        })
        return cleaned_data

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        return user
