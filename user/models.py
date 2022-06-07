from django.contrib.auth.models import AbstractUser
from django.db import models
from beer.models import Beer


class User(AbstractUser):
    class Meta:
        db_table = "User"

    favorite_beer = models.ManyToManyField(Beer, related_name='lover')
