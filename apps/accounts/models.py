from django.contrib.auth.models import AbstractUser
from django.db import models


# Custom user model, for future customization.
class User(AbstractUser):
    email = models.EmailField(
        'email address', blank=False, null=False, unique=True)
