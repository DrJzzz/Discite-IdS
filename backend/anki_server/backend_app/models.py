from django.db import models

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from backend_app.managers import CustomUserManager
from django.conf import settings

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])



class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    name = models.CharField(blank=True, max_length=100)
    birthdate = models.DateField(blank=True, null=True)
    max_reviews = models.IntegerField(blank=True, default=0)
    phone_number = models.CharField(blank=True, max_length=10, null=True)

    def __str__(self):
        return self.email
