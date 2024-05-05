from django.db import models
import os


def get_upload_path(instance, filename):
    return os.path.join('images', str(instance.pk), filename)

class Image(models.Model):
    image = models.ImageField(upload_to=get_upload_path, blank=True, null=True)

