# File that cleans the csv files
from datetime import datetime
import pandas as pd

# Remove the first column and rename certain teams to their current names
def cleanStats():
    stats = pd.read_csv('data/seasonstats.csv')
    stats = stats.drop(columns=['Unnamed: 0'], axis = 1, inplace=False)
    stats = stats.replace(to_replace=["Birmingham", "Small Heath"], value="Birmingham City")
    stats = stats.replace(to_replace="Newton Heath", value="Manchester Utd")
    stats = stats.replace(to_replace="Stoke", value="Stoke City")
    stats = stats.replace(to_replace="The Wednesday", value="Sheffield Weds")
    return stats

# Remove the id column and remove null matches. Also renames certain teams to their current names
def cleanMatches():
    matches = pd.read_csv('data/matches.csv')
    homeTeams = matches['Home']
    vals = homeTeams.isnull()
    for i in range(0, len(vals)):
        if vals[i]:
            matches = matches.drop(i)
    matches = matches.drop(columns=['Unnamed: 0'], axis = 1, inplace=False)
    #matches = matches.replace(to_replace=["Birmingham", "Small Heath"], value="Birmingham City")
    #matches = matches.replace(to_replace="Newton Heath", value="Manchester Utd")
    #matches = matches.replace(to_replace="Stoke", value="Stoke City")
    #matches = matches.replace(to_replace="The Wednesday", value="Sheffield Weds")
    return matches
                
# Remove the id column and then sort the teams alphabetically
def cleanTeams():
    teams = pd.read_csv('data/teams.csv')
    teams = teams.drop(teams.columns[0], axis = 1, inplace = False)
    teams = teams.sort_values('0')
    return teams
    
    
            
if __name__ == '__main__':
    #teams = cleanTeams()
    matches = cleanMatches()
    #stats = cleanStats()
    
    #print(teams)
    print(matches)
    #print(stats)
    
    #teams.to_csv('data/teams.csv')
    matches.to_csv('data/matches.csv')
    #stats.to_csv('data/seasonstats.csv')