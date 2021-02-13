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
    
    playerGoals = playerAssists = playerMinutes = playerPasses = playerTackles = 0
    goalieSaves = goalieCleansheets = 0

    if(data['data']['position_id'] == 1):
        for i in range(len(data['data']['stats']['data'])):
            try: 
                goalieSaves += data['data']['stats']['data'][i]['saves']
                goalieCleansheets += data['data']['stats']['data'][i]['cleansheets']
                playerMinutes += data['data']['stats']['data'][i]['minutes']
                playerPasses += data['data']['stats']['data'][i]['passes']['total']
                playerTackles += data['data']['stats']['data'][i]['tackles']
            except:
                playerPasses += 0
                playerTackles += 0
        
        
        formatted_data = [['Name', data['data']['display_name']],
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
        for i in range(len(data['data']['stats']['data'])):
            try: 
                playerGoals += data['data']['stats']['data'][i]['goals']
                playerAssists += data['data']['stats']['data'][i]['assists']
                playerMinutes += data['data']['stats']['data'][i]['minutes']
                playerPasses += data['data']['stats']['data'][i]['passes']['total']
                playerTackles += data['data']['stats']['data'][i]['tackles']
            except:
                playerPasses += 0
                playerTackles += 0
        
        
        formatted_data = [['Name', data['data']['display_name']],
                        ['Nationality', data['data']['nationality']],
                        ['Birth Date', data['data']['birthdate']],
                        ['Height', data['data']['height']],
                        ['Weight', data['data']['weight']],
                        ['Goals', playerGoals],
                        ['Assists', playerAssists],
                        ['Minutes', playerMinutes],
                        ['Passes', playerPasses],
                        ['Tackles', playerTackles]]

    df = pd.DataFrame(formatted_data, columns=['Attribute', 'Value'])
    print(df)


# getPlayerInfo(184941)
getPlayerInfo(186029)