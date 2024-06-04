from django.db import models

# Create your models here.
class seasonsTbl(models.Model):
    season = models.CharField(max_length=9, db_column="season")
    
class statsTbl(models.Model):
    season = models.CharField(max_length=9, db_column="season")
    squad = models.CharField(max_length=20, db_column="squad")
    wins = models.IntegerField(db_column="wins")
    draws = models.IntegerField(db_column="draws")
    losses = models.IntegerField(db_column="losses")
    goalsF = models.IntegerField(db_column="goalsFor")
    goalsA = models.IntegerField(db_column="goalsAgainst")
    points = models.IntegerField(db_column="points")
    shots = models.DecimalField(max_digits=5, decimal_places=1, db_column="shots")
    shotsOT = models.DecimalField(max_digits=5, decimal_places=1, db_column="shotsOT")
    FKShots = models.DecimalField(max_digits=4, decimal_places=1, db_column="FKShots")
    PKGoals = models.DecimalField(max_digits=4, decimal_places=1, db_column="PKGoals")
    cmp = models.DecimalField(max_digits=7, decimal_places=1, db_column="cmp")
    att = models.DecimalField(max_digits=7, decimal_places=1, db_column="att")
    cmpPerc = models.DecimalField(max_digits=4, decimal_places=1, db_column="cmpPerc")
    corners = models.DecimalField(max_digits=5, decimal_places=1, db_column="corners")
    crdY = models.DecimalField(max_digits=4, decimal_places=1, db_column="crdY")
    crdR = models.DecimalField(max_digits=3, decimal_places=1, db_column="crdR")
    fouls = models.DecimalField(max_digits=5, decimal_places=1, db_column="fouls")
    PKCon = models.DecimalField(max_digits=3, decimal_places=1, db_column="PKCon")
    ownGoals = models.DecimalField(max_digits=3, decimal_places=1, db_column="ownGoals")  