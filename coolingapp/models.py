from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()