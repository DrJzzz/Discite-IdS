from django.db import models
from django.contrib.auth.models import AbstractUser
from userapp.managers import CustomUserManager


import os 

def get_upload_path(instance, filename):
    return os.path.join('images', str(instance.pk), filename)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'birthdate']
    objects = CustomUserManager()
    name = models.CharField( max_length=100)
    birthdate = models.DateField( null=True)
    phone_number = models.CharField(default='00000000' ,max_length=12, null=True)
    
    picture = models.ImageField(upload_to=get_upload_path,
                                     blank=True,
                                     null=True,
                                     default='blank-user-picture.jpg')

    def __str__(self):
        return self.email
    

    
    
def get_default_user(sender, **kwargs):
        user, created = CustomUser.objects.get_or_create(
            email='default@default.com',
            name='default', 
            defaults=dict(birthdate='2001-01-01', 
                      password='pbkdf2_sha256$720000$gGKKPOvi9qRIZPSqeBJ2i3$+lg2RHb1upi9eMBLz+tgo9zqCgdYHsnktRNmHYOCzAM=', #1234
                      phone_number='0000000000')
        )
        
        return user
    
def create_default_user():
        user, created = CustomUser.objects.get_or_create(
            email='default@default.com',
            name='default', 
            defaults=dict(birthdate='2001-01-01', 
                      password='pbkdf2_sha256$720000$gGKKPOvi9qRIZPSqeBJ2i3$+lg2RHb1upi9eMBLz+tgo9zqCgdYHsnktRNmHYOCzAM=', 
                      phone_number='0000000000')
        )
        return user
    
    