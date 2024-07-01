from django.db import models

# Create your models here.
class upcomingMatches(models.Model):
    date = models.CharField(max_length=15, db_column="date")
    home = models.CharField(max_length=20, db_column="home")
    away =  models.CharField(max_length=20, db_column="away")
    venue = models.CharField(max_length=40, db_column="venue")