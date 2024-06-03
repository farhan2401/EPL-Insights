from django.db import models

# Create your models here.
class seasonsTbl(models.Model):
    season = models.CharField(max_length=9, db_column="season")