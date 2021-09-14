from django.db import models

class Memory(models.Model):
    date_created = models.DateField()
    club = models.CharField(max_length=100)
    course = models.TextField()
    weather = models.TextField()
    memory_details = models.TextField(max_length=5000)
    date_amended = models.DateField()
    is_current = models.BooleanField()
    owner = models.CharField(max_length=100)
