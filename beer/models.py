from django.db import models


class Beer(models.Model):
    class Meta:
        db_table = "Beer"

    name = models.CharField(max_length=256, default='')
    style = models.CharField(max_length=256, default='')
    category = models.CharField(max_length=256, default='')
    aroma = models.TextField(default='')
    flavor = models.TextField(default='')
    balance = models.TextField(default='')
    season = models.TextField(default='')
    paring_food = models.TextField(default='')
    body = models.TextField(default='')
    rating = models.IntegerField(default=0)
    img_url = models.TextField(default='')