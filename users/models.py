from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # We inherit username, email, password from AbstractUser
    major = models.CharField(max_length=100, blank=True)
    discord_handle = models.CharField(max_length=50, blank=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username
