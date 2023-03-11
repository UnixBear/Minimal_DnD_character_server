from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    favorite_class = models.CharField(max_length=40, blank=True)
