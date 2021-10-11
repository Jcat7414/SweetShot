from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    terms = models.BooleanField()
    created_on = models.DateField()

def __str__(self):
    return self.username