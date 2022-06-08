from django.db import models
from user.models import User
from beer.models import Beer


class History(models.Model):
    class Meta:
        db_table = "History"

    beer = models.ForeignKey(Beer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
