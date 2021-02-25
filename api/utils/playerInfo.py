import requests
import pandas as pd
import json
from .secrets import PLAYER_KEY, TEAM_KEY

# Takes player ID as input and returns nominal information of player in pandas dataframe
# DEV NOTE: Still need to consolidate and compute player statistics


def convertHeight(height):
    if height is None:
        return 0
    toConvert = int(height.split(" ", 1)[0])
    inches = toConvert * 0.393701
    feet = inches / 12
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
        return "1900-10-07"
    toConvert = date.split("/")
    return toConvert[2] + "-" + toConvert[1] + "-" + toConvert[0]


def getTeam(team_id):
    if team_id is None:
        return ""
    url = "https://football-pro.p.rapidapi.com/api/v2.0/teams/{}".format(
        team_id)

    querystring = {"tz": "Europe/Amsterdam"}

    headers = {
        'x-rapidapi-key': TEAM_KEY,
        'x-rapidapi-host': "football-pro.p.rapidapi.com"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    data = response.json()
    return data['data']["name"]


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

    appearances = goals = assists = yellow_cards = red_cards = tackles = fouls_committed = total_passes = pass_accuracy = saves = clean_sheets = penalties_saved = dribble_ratio = successful_dribbles = cross_ratio = successful_crosses = duels_ratio = successful_duels = key_passes = count = 0
    position = "Unknown Position"
    if data['data']['position_id'] == 1:
        position = "Goalkeeper"
    elif data['data']['position_id'] == 2:
        position = "Defender"
    elif data['data']['position_id'] == 3:
        position = "Midfielder"
    elif data['data']['position_id'] == 4:
        position = "Attacker"
    for i in range(len(player_data)):
        try:
            if player_data[i]['passes']['accuracy'] > 0:
                pass_accuracy += player_data[i]['passes']['accuracy']
                count += 1
            saves += player_data[i]['saves']
            clean_sheets += player_data[i]['cleansheets']
            penalties_saved += player_data[i]['penalties']['saves']
        except:
            pass_accuracy += 0

    if count == 0:
        pass_accuracy = 0
    else:
        pass_accuracy = pass_accuracy / count
    dribbleCount = crossCount = duelsCount = 0
    for i in range(len(player_data)):
        try:
            appearances += player_data[i]['appearences']
            goals += player_data[i]['goals']
            assists += player_data[i]['assists']
            yellow_cards += player_data[i]['yellowcards']
            red_cards += (player_data[i]['redcards'] +
                          player_data[i]['yellowred'])
            tackles += player_data[i]['tackles']
            fouls_committed += player_data[i]['fouls']['committed']
            total_passes += player_data[i]['passes']['total']
            if player_data[i]['dribbles']['attempts'] > 0:
                if player_data[i]['dribbles']['success'] == 0:
                    dribble_ratio += 0
                else:
                    dribble_ratio += (player_data[i]["dribbles"]["success"] /
                                      player_data[i]["dribbles"]["attempts"])
                dribbleCount += 1
            successful_dribbles += player_data[i]["dribbles"]["success"]
            if player_data[i]["crosses"]["total"] > 0:
                if player_data[i]["crosses"]["accurate"] == 0:
                    cross_ratio += 0
                else:
                    cross_ratio += (player_data[i]["crosses"]["accurate"] /
                                    player_data[i]["crosses"]["total"])
                crossCount += 1
            successful_crosses += player_data[i]["crosses"]["accurate"]
            if player_data[i]["duels"]["total"] > 0:
                if player_data[i]["duels"]["won"] == 0:
                    duels_ratio += 0
                else:
                    duels_ratio += (player_data[i]["duels"]["won"] /
                                    player_data[i]["duels"]["total"])
                duelsCount += 1
            successful_duels += player_data[i]["duels"]["won"]
            key_passes += player_data[i]["passes"]["key_passes"]
        except:
            total_passes += 0
            tackles += 0
            dribble_ratio += 0
            cross_ratio += 0
            duels_ratio += 0
    if dribbleCount == 0:
        dribble_ratio = 0
    else:
        dribble_ratio /= dribbleCount
    if crossCount == 0:
        cross_ratio = 0
    else:
        cross_ratio /= crossCount
    if duelsCount == 0:
        duels_ratio = 0
    else:
        duels_ratio /= duelsCount

    player_dataframe = [data['data']['team_id'],
                        data['data']['country_id'], position, data['data']['position_id'], convertDate(data['data']['birthdate']), convertHeight(data['data']['height']), convertWeight(data['data']['weight']), appearances, goals, assists, yellow_cards, red_cards, tackles, fouls_committed, total_passes, pass_accuracy, saves, clean_sheets, penalties_saved, dribble_ratio, successful_dribbles, cross_ratio, successful_crosses, duels_ratio, successful_duels, key_passes]
    index = ['team_id', 'country_id', 'position', 'position_id', 'birthdate', 'height', 'weight', 'appearances', 'goals', 'assists', 'yellow_cards', 'red_cards',
             'tackles', 'fouls_committed', 'total_passes', 'pass_accuracy', 'saves', 'clean_sheets', 'penalties_saved', 'dribble_ratio', 'successful_dribbles', 'cross_ratio', 'successful_crosses', 'duels_ratio', 'successful_duels', 'key_passes']

    df = pd.DataFrame(player_dataframe, index=index).to_dict()[0]
    return df
