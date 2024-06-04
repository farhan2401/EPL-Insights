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
    matches = matches[matches.Home is not None]
    matches = matches.drop(columns="Unnamed: 0", axis = 1, inplace = False)
    return matches
                
def cleanTeams():
    teams = pd.read_csv('data/teams.csv')
    teams = teams.drop(columns="Unnamed: 0", axis = 1, inplace = False)
    return teams
    
    
            
if __name__ == '__main__':
   # teams = cleanTeams()
    matches = cleanMatches()
    #stats = cleanStats()
    
   # print(teams.info())
    print(matches.info())
    #print(stats.info())
    
   # teams.to_csv('data/teams.csv')
    matches.to_csv('data/matches.csv')
    #stats.to_csv('data/seasonstats.csv')