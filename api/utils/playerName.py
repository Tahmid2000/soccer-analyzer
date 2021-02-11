import requests
import pandas as pd
import json
from .secrets import PLAYER_KEY

# Takes player name as input and returns player ID as integer
# DEV NOTE: Need to format player name (replace spaces with '%20')


def getPlayerName(name):
    url = "https://football-pro.p.rapidapi.com/api/v2.0/players/search/{}".format(
        name)

    querystring = {"tz": "Europe/Amsterdam"}

    headers = {
        'x-rapidapi-key': PLAYER_KEY,
        'x-rapidapi-host': "football-pro.p.rapidapi.com"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)  #

    data = response.json()['data']
    print(data)
    player_id = data[0]['player_id']
    return player_id


""" print(getPlayerName('ronaldo')) """


def getPlayers(name):
    url = "https://football-pro.p.rapidapi.com/api/v2.0/players/search/{}".format(
        name)

    querystring = {"tz": "Europe/Amsterdam"}

    headers = {
        'x-rapidapi-key': PLAYER_KEY,
        'x-rapidapi-host': "football-pro.p.rapidapi.com"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)  #

    data = response.json()['data']
    player_ids = []
    for player in data:
        player_info = {"player_id": player["player_id"],
                       "player_name": player["display_name"],
                       "image_path": player['image_path'],
                       "nationality": player['nationality']}
        player_ids.append(player_info)
    return player_ids


# print(getPlayers('neymar'))
