from django.db import models

# Create your models here.

class DataUji(models.Model):
    raw_data = models.TextField()
    cleaned_data = models.TextField(blank=True, null=True)
