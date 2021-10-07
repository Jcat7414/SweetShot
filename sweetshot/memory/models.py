from django.contrib.auth import get_user_model
from django.db import models

class Memory(models.Model):
    date_created = models.DateField()
    club = models.CharField(max_length=100)
    course = models.TextField()
    shot_date = models.DateField()
    weather = models.TextField()
    memory_details = models.TextField(max_length=5000)
    date_amended = models.DateField()
    is_current = models.BooleanField()
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owner_memory'
    )