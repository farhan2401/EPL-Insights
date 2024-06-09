# File that cleans the csv files
from datetime import datetime
import pandas as pd

# Import season stats
def cleanStats():
    stats = pd.read_csv('data/seasonstats.csv')
    stats = stats.drop(columns=['Unnamed: 0.2'], axis = 1, inplace=False)
    stats = stats.drop(stats.columns[0], axis=1, inplace=False)
    return stats

# Import matches
def cleanMatches():
    matches = pd.read_csv('data/matches.csv')
    homeTeams = matches['Home']
    vals = homeTeams.isnull()
    for i in range(0, len(vals)):
        if vals[i]:
            matches = matches.drop(i)
    matches = matches.drop(columns=['Unnamed: 0.2'], axis = 1, inplace=False)
    matches = matches.drop(matches.columns[0], axis=1, inplace=False)
    return matches
                
def cleanTeams():
    teams = pd.read_csv('data/teams.csv')
    teams = teams.sort_values('0')
    teams = teams.drop(teams.columns[0], axis = 1, inplace = False)
    return teams
    
    
            
if __name__ == '__main__':
    teams = cleanTeams()
    matches = cleanMatches()
    stats = cleanStats()
    
    print(teams)
    print(matches)
    print(stats)
    
    teams.to_csv('data/teams.csv')
    matches.to_csv('data/matches.csv')
    stats.to_csv('data/seasonstats.csv')