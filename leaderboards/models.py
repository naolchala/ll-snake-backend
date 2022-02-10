from django.db import models

# Create your models here.
class Score(models.Model):
    username = models.CharField(max_length=200)
    points = models.IntegerField(default=0)