import requests
import pandas as pd
import json
from .secrets import TEAM_KEY


def getFixtures(data, id1, id2):
    fixtures = data["fixtures"]
    fixture_ids = []
    for fixture in fixtures:
        fixture_info = {"id1": id1, "id2": id2, "league": fixture["league"]["name"], "date": fixture["event_date"], "round": fixture["round"], "status": fixture["statusShort"],
                        "venue": fixture["venue"], "home_logo": fixture['homeTeam']["logo"], "away_logo": fixture['awayTeam']["logo"], "score": fixture["score"]["fulltime"]}
        fixture_ids.append(fixture_info)
    return fixture_ids


def getStats(data, id1, id2):
    teams = data["teams"]
    total_games = teams[0]['statistics']['played']['total']
    
    home_id1_games = teams[0]['statistics']['played']['home']
    away_id1_games = teams[0]['statistics']['played']['away']
    home_id1_wins = teams[0]['statistics']['wins']['home']
    away_id1_wins = teams[0]['statistics']['wins']['away']
    home_id1_draws = teams[0]['statistics']['draws']['home']
    away_id1_draws = teams[0]['statistics']['draws']['away']
    home_id1_losses = teams[0]['statistics']['loses']['home']
    away_id1_losses = teams[0]['statistics']['loses']['away']

    home_id2_games = teams[1]['statistics']['played']['home']
    away_id2_games = teams[1]['statistics']['played']['away']
    home_id2_wins = teams[1]['statistics']['wins']['home']
    away_id2_wins = teams[1]['statistics']['wins']['away']
    home_id2_draws = teams[1]['statistics']['draws']['home']
    away_id2_draws = teams[1]['statistics']['draws']['away']
    home_id2_losses = teams[1]['statistics']['loses']['home']
    away_id2_losses = teams[1]['statistics']['loses']['away']
    home_id1_goals_for = home_id1_goals_against = away_id1_goals_for = away_id1_goals_against = 0
    home_id2_goals_for = home_id2_goals_against = away_id2_goals_for = away_id2_goals_against = 0
    fixtures = data["fixtures"]

    for fixture in fixtures:
        try:
            if fixture["homeTeam"]["team_id"] == id1:
                home_id1_goals_for += fixture["goalsHomeTeam"]
                home_id1_goals_against += fixture["goalsAwayTeam"]
                away_id2_goals_against += fixture["goalsHomeTeam"]
                away_id2_goals_for += fixture["goalsAwayTeam"]
            else:
                home_id2_goals_for += fixture["goalsHomeTeam"]
                home_id2_goals_against += fixture["goalsAwayTeam"]
                away_id1_goals_against += fixture["goalsHomeTeam"]
                away_id1_goals_for += fixture["goalsAwayTeam"]
        except:
            home_id1_goals_for += 0
            home_id1_goals_against += 0
            away_id2_goals_against += 0
            away_id2_goals_for += 0
            home_id2_goals_for += 0
            home_id2_goals_against += 0
            away_id1_goals_against += 0
            away_id1_goals_for += 0

    statistics_dataframe = [id1, id2, total_games, home_id1_games,
                            away_id1_games, home_id1_wins, away_id1_wins, home_id1_draws, away_id1_draws, home_id1_losses, away_id1_losses, home_id1_goals_for, home_id1_goals_against, away_id1_goals_for, away_id1_goals_against, home_id2_games, away_id2_games, home_id2_wins, away_id2_wins, home_id2_draws, away_id2_draws, home_id2_losses, away_id2_losses, home_id2_goals_for, home_id2_goals_against, away_id2_goals_for, away_id2_goals_against]
    index = ['id1', 'id2', 'total_games', 'home_id1_games',
             'away_id1_games', 'home_id1_wins', 'away_id1_wins', 'home_id1_draws', 'away_id1_draws', 'home_id1_losses', 'away_id1_losses', 'home_id1_goals_for', 'home_id1_goals_against', 'away_id1_goals_for', 'away_id1_goals_against', 'home_id2_games', 'away_id2_games', 'home_id2_wins', 'away_id2_wins', 'home_id2_draws', 'away_id2_draws', 'home_id2_losses', 'away_id2_losses', 'home_id2_goals_for', 'home_id2_goals_against', 'away_id2_goals_for', 'away_id2_goals_against']
    df = pd.DataFrame(statistics_dataframe, index=index).to_dict()[0]
    return df


def teamsInfo(id1, id2):
    url = "https://api-football-v1.p.rapidapi.com/v2/fixtures/h2h/{}/{}".format(
        id1, id2)

    headers = {
        'x-rapidapi-key': TEAM_KEY,
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    data = response.json()["api"]
    return {"stats": getStats(data, id1, id2), "fixtures": getFixtures(data, id1, id2)}
