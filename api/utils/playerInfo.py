import requests
import pandas as pd
import json
from .secrets import PLAYER_KEY

# Takes player ID as input and returns nominal information of player in pandas dataframe
# DEV NOTE: Still need to consolidate and compute player statistics


def convertHeight(height):
    if height is None:
        return 0
    toConvert = int(height.split(" ", 1)[0])
    inches = toConvert*0.393701
    feet = inches/12
    i = 0
    while feet >= 1:
        i += 1
        feet -= 1
    inches2 = feet*12
    result = "" + str(i) + "'" + str(inches2) + "\""
    return round(inches)


def convertWeight(weight):
    if weight is None:
        return 0
    toConvert = int(weight.split(" ", 1)[0])
    return round(toConvert * 2.20462)


def convertDate(date):
    if date is None:
        return "2000-10-07"
    toConvert = date.split("/")
    return toConvert[2] + "-" + toConvert[1] + "-" + toConvert[0]


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

    appearances = goals = assists = yellow_cards = red_cards = tackles = fouls_committed = total_passes = pass_accuracy = saves = clean_sheets = penalties_saved = 0

    for i in range(len(player_data)):
        try:
            appearances += player_data[i]['appearences']
            goals += player_data[i]['goals']
            assists += player_data[i]['assists']
            yellow_cards += player_data[i]['yellowcards']
            red_cards += player_data[i]['redcards'] + \
                player_data[i]['yellowred']
            tackles += player_data[i]['tackles']
            fouls_committed += player_data[i]['fouls']['committed']
            total_passes += player_data[i]['passes']['total']
            pass_accuracy += player_data[i]['passes']['accurate']
            saves += player_data[i]['saves']
            clean_sheets += player_data[i]['cleansheets']
            penalties_saved += player_data[i]['penalties']['saves']
        except:
            total_passes += 0
            tackles += 0

    player_dataframe = [data['data']['team_id'],
                        data['data']['country_id'], data['data']['position_id'], convertDate(data['data']['birthdate']), convertHeight(data['data']['height']), convertWeight(data['data']['weight']), appearances, goals, assists, yellow_cards, red_cards, tackles, fouls_committed, total_passes, pass_accuracy, saves, clean_sheets, penalties_saved]
    index = ['team_id', 'country_id', 'position_id', 'birthdate', 'height', 'weight', 'appearances', 'goals', 'assists', 'yellow_cards', 'red_cards',
             'tackles', 'fouls_committed', 'total_passes', 'pass_accuracy', 'saves', 'clean_sheets', 'penalties_saved']

    df = pd.DataFrame(player_dataframe, index=index).to_dict()[0]
    return df


""" getPlayerInfo(184941) """
