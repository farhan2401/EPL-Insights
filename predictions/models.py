from django.db import models

# Create your models here.
class upcomingMatches(models.Model):
    date = models.CharField(max_length=15, db_column="date")
    week = models.IntegerField()
    homeTeam = models.CharField(max_length=20, db_column="home")
    awayTeam =  models.CharField(max_length=20, db_column="away")
    venue = models.CharField(max_length=40, db_column="venue")
    
class upcomingPreds(models.Model):
    date = models.CharField(max_length=15, db_column="date")
    week = models.IntegerField()
    homeTeam = models.CharField(max_length=20, db_column="home")
    home = models.DecimalField(max_digits=4, decimal_places=2, db_column='homePred')
    draw = models.DecimalField(max_digits=4, decimal_places=2, db_column='drawPred')
    away = models.DecimalField(max_digits=4, decimal_places=2, db_column='awayPred')
    awayTeam =  models.CharField(max_length=20, db_column="away")
    venue = models.CharField(max_length=40, db_column="venue")