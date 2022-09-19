from django.db import models
from helpers.models import TrackingModel
from django.contrib.auth.models import (PermissionsMixin, AbstractBaseUser) 

from celeryApp.managers import CustomUserManager

from django.utils.translation import gettext as _
from django.utils import timezone
from django.core.validators import RegexValidator

import jwt
from datetime import datetime, timedelta

from django.conf import settings
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin, TrackingModel):
    username = models.CharField(max_length=258)
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    phone_regex = RegexValidator(regex=r'^\d{10}$', message="Phone number should exactly be in 10 digits")
    phone = models.CharField(max_length=255, validators=[phone_regex], blank=True, null=True)

    EMAIL_FIELD = 'eamil'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    @property
    def token(self):
        token = jwt.encode(
            {'username': self.username, 'email': self.email, 'exp':datetime.now() + timedelta(hours=24)},
            settings.SECRET_KEY, algorithm='HS256')
        return token
