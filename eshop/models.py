# from random import choices
# from secrets import choice
from django.db import models
from django.contrib.auth.models import AbstractUser
from enum import Enum
# from django_mysql.models import EnumField
from .manager import *



class Choice(Enum):
    one = '1'
    zero = '0'

class RegistrationChoice(Enum):
    Normal ='N'
    Facebook ='F'
    Twitter ='T'
    Google = 'G'

class CustomUser(AbstractUser):
    username = None
    # first_name = models.CharField(max_length=45)
    # last_name = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    status = models.CharField(max_length=12, choices=[(x, x.value) for x in Choice])
    # status = models.EnumField(choices=Choice.choices)
    created_date = models.DateField(auto_now=True)
    fb_token = models.CharField(max_length=100)
    twitter_token = models.CharField(max_length=100)
    google_token = models.CharField(max_length=100)
    # registration_method = models.EnumField(choices=RegistrationChoice.choices)
    registration_method = models.CharField(max_length=34, choices=[(y, y.value) for y in RegistrationChoice])

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



