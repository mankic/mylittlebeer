from django.contrib.auth.models import AbstractUser
from django.db import models
from beer.models import Beer
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


class User(AbstractUser):
    class Meta:
        db_table = "User"
    email = models.EmailField(_('email address'), unique=True)

    favorite_beer = models.ManyToManyField(Beer, related_name='lover')

