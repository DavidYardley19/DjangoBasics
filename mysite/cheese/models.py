from django.db import models

# Create your models here.
class Cheese(models.Model):
    name = models.CharField(max_length=200)
    rating = models.IntegerField()