from django.db import models

# Create your models here.
class seasonsTbl(models.Model):
    season = models.CharField(max_length=9, db_column="season")
    
class teamsTbl(models.Model):
    squad = models.CharField(max_length=20, db_column="squad")
    
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
    
class matchesTbl(models.Model):
    season = models.CharField(max_length=9, db_column="season")
    date = models.CharField(max_length=15, db_column="date")
    home = models.CharField(max_length=20, db_column="home")
    homeXG = models.DecimalField(max_digits=3, decimal_places=1, db_column="homeXG")
    homeGoals = models.IntegerField(db_column="homeGoals")
    awayGoals = models.IntegerField(db_column="awayGoals")
    awayXG = models.DecimalField(max_digits=3, decimal_places=1)
    away =  models.CharField(max_length=20, db_column="away")
    attendance = models.IntegerField(db_column="attendance")
    venue = models.CharField(max_length=40, db_column="venue")
    
class currTbl(models.Model):
    position = models.IntegerField(db_column="positon")
    squad = models.CharField(max_length=20, db_column="squad")
    played = models.IntegerField(db_column="played")
    wins = models.IntegerField(db_column="wins")
    draws = models.IntegerField(db_column="draws")
    losses = models.IntegerField(db_column="losses")
    gf = models.IntegerField(db_column="goalsF")
    ga = models.IntegerField(db_column="goalsA")
    gd = models.IntegerField(db_column="goalD")
    points = models.IntegerField(db_column="points")