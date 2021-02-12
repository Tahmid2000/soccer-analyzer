import requests
import pandas as pd
import json
from secrets import PLAYER_KEY

# Takes player ID as input and returns nominal information of player in pandas dataframe
# DEV NOTE: Still need to consolidate and compute player statistics


def getPlayerInfo(player_id):
    url = "https://football-pro.p.rapidapi.com/api/v2.0/players/{}".format(
        player_id)

    querystring = {"include": "stats", "tz": "Europe/Amsterdam"}

    headers = {
        'x-rapidapi-key': PLAYER_KEY,
        'x-rapidapi-host': "football-pro.p.rapidapi.com"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    data = response.json()

    playerGoals = 0
    for i in range(len(data['data']['stats']['data'])):
        playerGoals += data['data']['stats']['data'][i]['goals']

    playerAssists = 0
    for i in range(len(data['data']['stats']['data'])):
        playerAssists += data['data']['stats']['data'][i]['assists']
    
    formatted_data = [['Name', data['data']['display_name']],
                      ['Nationality', data['data']['nationality']],
                      ['Birth Date', data['data']['birthdate']],
                      ['Height', data['data']['height']],
                      ['Weight', data['data']['weight']],
                      ['Goals', playerGoals],
                      ['Assists', playerAssists]]

    df = pd.DataFrame(formatted_data, columns=['Attribute', 'Value'])
    print(df)


getPlayerInfo(580)
