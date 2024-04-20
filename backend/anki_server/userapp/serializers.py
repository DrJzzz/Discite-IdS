from django.contrib.auth.models import Group, User
from rest_framework import serializers
from userapp.models import CustomUser
from exarth_rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from allauth.account.forms import SignupForm
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email','name', 'birthdate', 'max_reviews', 'phone_number']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
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

    def get_form_class(self):
        return CustomSignupForm

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        return user

class CustomSignupForm(SignupForm):
    # Elimina el campo username del formulario
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'username' in self.fields:
            del self.fields['username']