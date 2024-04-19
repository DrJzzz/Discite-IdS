from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
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