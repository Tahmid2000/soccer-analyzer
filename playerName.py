import requests
import pandas as pd
import json


# Takes player name as input and returns player ID as integer
# DEV NOTE: Need to format player name (replace spaces with '%20')

def getPlayerName(name):
    url = "https://football-pro.p.rapidapi.com/api/v2.0/players/search/{}".format(name)

    querystring = {"tz":"Europe/Amsterdam"}

    headers = {
        'x-rapidapi-key': "d23bab6737mshb845a2338eedcb2p137711jsnf78fa2d0de2f",
        'x-rapidapi-host': "football-pro.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.json()['data']
    player_id = data[0]['player_id']
    return player_id

getPlayerName('Lionel%20Messi')