from django.db import models

# Create your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class PhoneClient(models.Model):
    """model for phone client database for PhoneClient"""
    ph_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(default=0)
    client_name = models.CharField(max_length=30)
    # phone_number = models.IntegerField(max_length=10,default="")
    subject = models.CharField(max_length = 128)
    gist = models.TextField(default="")

class ChatClient(models.Model):
    """model for phone client database for PhoneClient"""
    ch_d = models.AutoField(primary_key=True)
    user_id = models.IntegerField(default=0)
    client_name = models.CharField(max_length=30)
    subject = models.CharField(max_length = 128)
    gist = models.TextField(default="")
