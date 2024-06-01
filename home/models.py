from django.db import models

# Create your models here.
class seasonStats (models.Model):
    id = models.BigAutoField(primary_key = True)
    Season = models.CharField(max_length = 9)
    Squad = models.CharField(max_length = 25)
    W = models.IntegerField()
    D = models.IntegerField()
    L = models.IntegerField()
    GF = models.IntegerField()
    GA = models.IntegerField()
    Pts = models.IntegerField()
    Sh = models.IntegerField()
    SoT = models.IntegerField()
    FK = models.IntegerField()
    PK = models.IntegerField()
    Cmp = models.IntegerField()
    Att = models.IntegerField()
    CmpPerc = models.DecimalField(max_digits=4, decimal_places=1, db_column = 'Cmp%')
    CK = models.IntegerField()
    CrdY = models.IntegerField()
    CrdR = models.IntegerField()
    Fls = models.IntegerField()
    PKcon = models.IntegerField()
    OG = models.IntegerField()
    
class matches(models.Model):
    Season = models.CharField(max_length = 9)
    Date = models.DateField()
    Home = models.CharField(max_length = 25)
    homexG = models.DecimalField(max_digits = 3, decimal_places = 1, db_column = 'xG')
    homeGoals = models.IntegerField(db_column = 'Home Goals')
    awayGoals = models.IntegerField(db_column = 'Away Goals')
    awayxG = models.DecimalField(max_digits = 3, decimal_places = 1, db_column = 'xG.1')
    Away = models.CharField(max_length = 25)
    Attendance = models.IntegerField()
    Venue = models.CharField(max_length = 50)

class teams(models.Model):
    id = models.BigAutoField(primary_key = True)
    team = models.CharField(max_length = 25)
    
class seasons(models.Model):
    id = models.BigAutoField(primary_key = True)
    season = models.CharField(max_length = 9)