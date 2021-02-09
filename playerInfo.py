import requests
import pandas as pd
import json

# Takes player ID as input and returns nominal information of player in pandas dataframe
# DEV NOTE: Still need to consolidate and compute player statistics

def getPlayerInfo(player_id):
    url = "https://football-pro.p.rapidapi.com/api/v2.0/players/{}".format(player_id)

    querystring = {"include":"stats","tz":"Europe/Amsterdam"}

    headers = {
        'x-rapidapi-key': "d23bab6737mshb845a2338eedcb2p137711jsnf78fa2d0de2f",
        'x-rapidapi-host': "football-pro.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    formatted_data = [['Name', data['data']['display_name']],
                    ['Nationality', data['data']['nationality']],
                    ['Birth Date', data['data']['birthdate']],
                    ['Height', data['data']['height']],
                    ['Weight', data['data']['weight']]]

    df = pd.DataFrame(formatted_data, columns = ['Attribute', 'Value'])
    print(df)

getPlayerInfo(184798)

