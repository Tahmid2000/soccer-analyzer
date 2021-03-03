import requests
import json
from .secrets import PLAYER_KEY


def getPlayers(name):
    url = "https://football-pro.p.rapidapi.com/api/v2.0/players/search/{}".format(
        name)

    querystring = {"tz": "Europe/Amsterdam"}

    headers = {
        'x-rapidapi-key': PLAYER_KEY,
        'x-rapidapi-host': "football-pro.p.rapidapi.com"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    data = response.json()['data']
    player_ids = []
    for player in data:
        player_info = {"player_id": player["player_id"],
                       "player_name": player["display_name"],
                       "image_path": player['image_path'],
                       "nationality": player['nationality']}
        player_ids.append(player_info)
    return player_ids
