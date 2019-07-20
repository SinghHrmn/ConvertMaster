from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MyConversion(models.Model):
    user = models.ForeignKey(User, on_delete='Cascade')
    original = models.CharField(max_length=4)
    converted = models.CharField(max_length=4)
    filename = models.CharField(max_length=20, unique=True)
    convName = models.CharField(max_length=50)
    