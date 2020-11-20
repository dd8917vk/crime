from django.db import models
from django.conf import settings
# Create your models here.

class Departments(models.Model):
    agency_name = models.CharField(max_length=200)
    state_name = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100, null=True, blank=True)
    longitude = models.CharField(max_length=100, null=True, blank=True)

