# Code for this model was taken and modified fromDavid Sheehan
# https://dashee87.github.io/football/python/predicting-football-results-with-statistical-modelling/
import sqlite3
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np
import seaborn
from scipy.stats import poisson,skellam

# Create a connection to the database and get the upcoming matches and past matches
cnx = sqlite3.connect('db.sqlite3')
upcoming = pd.read_sql_query("SELECT * FROM predictions_upcomingmatches", cnx)
pastMatches = pd.read_sql_query("SELECT home, homeGoals, awayGoals, away FROM home_matchestbl", cnx)

# Build the model
goal_model_data = pd.concat([pastMatches[['home', 'away', 'homeGoals']].rename(
    columns={'home':'team', 'away':'opponent', 'homeGoals':'goals'}).assign(home=1),
    pastMatches[['away', 'home', 'awayGoals']].rename(
    columns={'away':'team', 'home':'opponent', 'awayGoals':'goals'}).assign(home=0)
])
poisson_model = smf.glm(formula="goals ~ home + team + opponent", data=goal_model_data, 
                        family=sm.families.Poisson()).fit()

# Create a method to predict the number of goals for each team
def simulateMatch(model, homeTeam, awayTeam, max_goals=10):
    homeGoals_avg = model.predict(pd.DataFrame(data={'team':homeTeam,
                                                     'opponent':awayTeam, 'home':1}, index=[1])).values[0]
    awayGoals_avg = model.predict(pd.DataFrame(data={'team':awayTeam,
                                                     'opponent':homeTeam, 'home':0}, index=[1])).values[0]
    teampred = [[poisson.pmf(i, team_avg) for i in range (0, max_goals + 1)] for team_avg in [homeGoals_avg, awayGoals_avg]]
    return (np.outer(np.array(teampred[0]), np.array(teampred[1])))

# Create a method to predict all upcoming matches
def predictUpcoming(model, upcoming):
    # Create a dataframe to add the results to
    results = pd.DataFrame(columns=['homeTeam', 'Home', 'Draw', 'Away', 'awayTeam'])
    # Go through each match and calculate the probability of home team win, draw, and away team win
    for index in range(0, len(upcoming.index)):
        row = upcoming.iloc[[index]].values
        print(row)
        homeTeam = row[0][2]
        awayTeam = row[0][3]
        matchRes = simulateMatch(model, homeTeam, awayTeam, max_goals=10)
        homeProb = np.sum(np.tril(matchRes, -1))
        drawProb = np.sum(np.diag(matchRes))
        awayProb = np.sum(np.triu(matchRes, 1))
        # Create a data frame storing the results from this match
        resultDf = pd.DataFrame(data={'homeTeam':homeTeam, 'Home':[f"{homeProb:.2%}"], 'Draw':[f"{drawProb:.2%}"],
                                    'Away':[f"{awayProb:.2%}"], 'awayTeam':awayTeam})
        # Append to the main dataframe
        results = results._append(resultDf)
    return results

def main():
    matchPred = predictUpcoming(poisson_model, upcoming)
    print(matchPred)
    
if (__name__ == "__main__"):
    main()