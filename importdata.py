# File that imports all data from the CSV files into the models

import csv
from datetime import datetime
from home.models import *

# Import season stats
def importStats(filePath):
    with open(filePath, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            seasonStats.objects.create(
                season = row['Season'],
                team = row['Squad'],
                wins = row['W'],
                draws = row['D'],
                losses = row['L'],
                goalsF = row['GF'],
                goalsA = row['GA'],
                points = row['Pts'],
                shots = row['Sh'],
                shotsOT = row['SoT'],
                freeK = row['FK'],
                PKGoals = row['PK'],
                passCmp = row['Cmp'],
                passAtt = row['Att'],
                passPerc = row['Cmp%'],
                corners = row['CK'],
                yellows = row['CrdY'],
                reds = row['CrdR'],
                fouls = row['Fls'],
                PKCon = row['PKcon'],
                ownGoals = row['OG']
            )

# Import matches
def importMatches(filePath):
    with open(filePath, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            matches.objects.create(
                season = row['Season'],
                date = row['Date'],
                home = row['Home'],
                homexG = row['xG'],
                homeGoals = row['Home Goals'],
                awayGoals = row['Away Goals'],
                awayxG = row['xG.1'],
                away = row['Away'],
                attendance = row['Attendance'],
                venue = row['Venue']
            )

# Import seasons
def importSeasons(filePath):
    with open(filePath, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            seasons.objects.create(
                season = row['0']
            )
            
def importTeams(filePath):
    with open(filePath, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            teams.objects.create(
                team = row['0']
            )
            
if __name__ == '__main__':
    importTeams('data/teams.csv')
    importSeasons('data/seasons.csv')
    importMatches('data/matches.csv')
    importStats('data/seasonstats.csv')