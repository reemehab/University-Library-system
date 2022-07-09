from django.db import models
from django.contrib.auth.models import User
from django.db.models.aggregates import Min
from django.db.models.base import Model
from django.db.models.enums import Choices
from django.db.models.fields import BLANK_CHOICE_DASH, DateField
# Create your models here.

class Profile(models.Model):
    username = models.CharField(max_length=50)
    birthDate = models.DateField()
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField()
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    profileID = models.IntegerField(default=True)

class Book(models.Model):
    ID=models.IntegerField(primary_key=True,default=True)
    title = models.CharField(max_length=250,null=True, blank=True)
    author = models.CharField(max_length=250,null=True, blank=True)
    ISBN =models.CharField(max_length=50,null=True, blank=True)
    borrowing_period = models.CharField(max_length=50 ,null=True, blank=True)
    status = models.BooleanField(default=True,null=False, blank=False)
    Publication_Year=models.DateField(null=True)
    Category=models.CharField(max_length=50 ,null=True, blank=True)
    Publisher=models.CharField(max_length=50,null=True, blank=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True, blank=True)
    def str(self):
       return self.cat
