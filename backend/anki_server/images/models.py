from django.db import models
import os
from userapp.models import CustomUser, create_default_user

def get_upload_path(instance, filename):
    return os.path.join('images', str(instance.owner.pk), filename)

class Image(models.Model):
    
    image = models.ImageField(upload_to=get_upload_path, blank=True, null=True)
    owner = models.ForeignKey('userapp.CustomUser', 
                              related_name='image_owner',
                              on_delete=models.CASCADE,
                              default=create_default_user)


