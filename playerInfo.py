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
    player_data = data['data']['stats']['data']
    position_id = data['data']['position_id']
    
    playerGoals = playerAssists = playerMinutes = playerPasses = playerTackles = 0
    goalieSaves = goalieCleansheets = 0

    if (position_id == 1):
        for i in range(len(player_data)):
            try: 
                goalieSaves += player_data[i]['saves']
                goalieCleansheets += player_data[i]['cleansheets']
                playerMinutes += player_data[i]['minutes']
                playerPasses += player_data[i]['passes']['total']
                playerTackles += player_data[i]['tackles']
            except:
                playerPasses += 0
                playerTackles += 0
        
        
        player_dataframe = [['Name', data['data']['display_name']],
                        ['Nationality', data['data']['nationality']],
                        ['Birth Date', data['data']['birthdate']],
                        ['Height', data['data']['height']],
                        ['Weight', data['data']['weight']],
                        ['Saves', goalieSaves],
                        ['Cleansheets', goalieCleansheets],
                        ['Minutes', playerMinutes],
                        ['Passes', playerPasses],
                        ['Tackles', playerTackles]]
    else:
        for i in range(len(player_data)):
            try: 
                playerGoals += player_data[i]['goals']
                playerAssists += player_data[i]['assists']
                playerMinutes += player_data[i]['minutes']
                playerPasses += player_data[i]['passes']['total']
                playerTackles += player_data[i]['tackles']
            except:
                playerPasses += 0
                playerTackles += 0
        
        
        player_dataframe = [['Name', data['data']['display_name']],
                        ['Nationality', data['data']['nationality']],
                        ['Birth Date', data['data']['birthdate']],
                        ['Height', data['data']['height']],
                        ['Weight', data['data']['weight']],
                        ['Goals', playerGoals],
                        ['Assists', playerAssists],
                        ['Minutes', playerMinutes],
                        ['Passes', playerPasses],
                        ['Tackles', playerTackles]]

    df = pd.DataFrame(player_dataframe, columns=['Attribute', 'Value'])
    print(df)


getPlayerInfo(184941)
# getPlayerInfo(186029)