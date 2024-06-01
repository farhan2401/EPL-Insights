# File that cleans the csv files
from datetime import datetime
import pandas as pd

# Import season stats
def cleanStats():
    stats = pd.read_csv('data/seasonstats.csv')
    stats = stats.drop(columns="Unnamed: 0", axis = 1, inplace = False)
    return stats

# Import matches
def cleanMatches():
    matches = pd.read_csv('data/matches.csv')
    matches = matches.drop(columns="Unnamed: 0", axis = 1, inplace = False)
    return matches

# Import seasons
def cleanSeasons():
    seasons = pd.read_csv('data/seasons.csv')
    seasons = seasons.drop(columns="Unnamed: 0", axis = 1, inplace = False)
    return seasons
                
def cleanTeams():
    teams = pd.read_csv('data/teams.csv')
    teams = teams.drop(columns="Unnamed: 0", axis = 1, inplace = False)
    return teams
    
    
            
if __name__ == '__main__':
    teams = cleanTeams()
    seasons = cleanSeasons()
    matches = cleanMatches()
    stats = cleanStats()
    
    print(teams.info())
    print(seasons.info())
    print(matches.info())
    print(stats.info())
    
    teams.to_csv('data/teams.csv')
    seasons.to_csv('data/seasons.csv')
    matches.to_csv('data/matches.csv')
    stats.to_csv('data/seasonstats.csv')