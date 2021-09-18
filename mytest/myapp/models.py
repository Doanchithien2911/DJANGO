from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model
from django.db.models.fields import IntegerField
from django.conf import settings

class User(AbstractUser):
    username = models.CharField(null=False,unique=True,max_length=255)
    email = models.EmailField(null=False,unique=True,max_length=255)
    password = models.CharField(null=False,max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username
    
class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    user_id = models.IntegerField()
    date_complete = models.DateField()
    status = models.CharField(null=False,max_length=20)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

