from django.db import models
from django.contrib.auth.models import AbstractUser
from userapp.managers import CustomUserManager

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'birthdate']
    objects = CustomUserManager()
    name = models.CharField( max_length=100)
    birthdate = models.DateField( null=True)
    max_reviews = models.IntegerField( default=0)
    phone_number = models.CharField(default='00000000' ,max_length=12, null=True)

    def __str__(self):
        return self.email
    
    def create_default_user():
        user, created = CustomUser.objects.get_or_create(
            email='default@default.com',
            name='default', 
            defaults=dict(birthdate='2001-01-01', 
                      password='password1234.', 
                      phone_number='0000000000')
        )

        return user
    
    def get_default_user():
        return User.objects.get(email='default@default.com').id
    
def get_default_user(sender, **kwargs):
        user, created = CustomUser.objects.get_or_create(
            email='default@default.com',
            name='default', 
            defaults=dict(birthdate='2001-01-01', 
                      password='password1234.', 
                      phone_number='0000000000')
        )
        
        return user
    
def create_default_user():
        user, created = CustomUser.objects.get_or_create(
            email='default@default.com',
            name='default', 
            defaults=dict(birthdate='2001-01-01', 
                      password='password1234.', 
                      phone_number='0000000000')
        )
        return user
    
    
    