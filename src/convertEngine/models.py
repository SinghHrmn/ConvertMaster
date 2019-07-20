from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MyConversion(models.Model):
    methods = [
        ('xml' , 'XML'),
        ('json', 'JSON'),
        ('csv', 'CSV')
    ]
    user = models.ForeignKey(User, on_delete='Cascade')
    original = models.CharField(max_length=4, choices=methods)
    converted = models.CharField(max_length=4, choices=methods)
    filename = models.CharField(max_length=20, unique=True)
    convName = models.CharField(max_length=50)
    