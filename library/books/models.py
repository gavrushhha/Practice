from django.conf import settings
from django.db import models
from django.utils import timezone

class Books(models.Model):
    author=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    year_of_create=models.CharField(max_length=50)
    publishing=models.CharField(max_length=150)
    def __str__(self):
        return self.title