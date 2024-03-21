from django.db import models


class Animation(models.Model):
    name = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    price = models.IntegerField()
    pga = models.IntegerField(blank=True)
