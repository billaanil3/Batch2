from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from django.core.validators import RegexValidator

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from .managers import CustomUserManager


# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(_('email address'), unique=True)
#     name = models.CharField(max_length=255)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     date_joined = models.DateTimeField(default=timezone.now)

#     phone_regex = RegexValidator(regex=r'^\d{10}$', message="Phone number should exactly be in 10 digits")
#     phone = models.CharField(max_length=255, validators=[phone_regex], blank=True, null=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email

# class CustomUser(AbstractUser):
#     is_director = models.BooleanField(default=False)
#     is_producer = models.BooleanField(default=True)