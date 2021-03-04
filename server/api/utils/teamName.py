import requests
import json
from .secrets import TEAM_KEY


def getTeams(name):
    name = name.replace(" ", "%20")
    url = "https://api-football-v1.p.rapidapi.com/v2/teams/search/{}".format(
        name)

    headers = {
        'x-rapidapi-key': TEAM_KEY,
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com"
    }
    team_ids = []
    try:
        response = requests.request("GET", url, headers=headers)
        data = response.json()["api"]["teams"]
    except requests.exceptions.RequestException as e:
        return team_ids
    for team in data:
        team_info = {
            "team_id": team["team_id"], "team_name": team["name"], "image_path": team["logo"], "founded": team["founded"], "country": team["country"], "venue_name": team["venue_name"]}
        team_ids.append(team_info)
    return team_ids
