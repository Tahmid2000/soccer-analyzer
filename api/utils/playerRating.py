import pandas as pd
from .playerInfo import *


def playerRating(player_id):

    df = getPlayerInfo(player_id)
    appearances = df['appearances']
    goals_ratio = df['goals'] / appearances
    assists_ratio = df['assists'] / appearances
    total_passes_ratio = df['total_passes'] / appearances
    saves_ratio = df['saves'] / appearances
    clean_sheets_ratio = df['clean_sheets'] / appearances
    penalties_saved_ratio = df['penalties_saved'] / appearances
    tackles_ratio = df['tackles'] / appearances
    yellow_cards_ratio = df['yellow_cards'] / appearances
    red_cards_ratio = df['red_cards'] / appearances
    fouls_committed_ratio = df['fouls_committed'] / appearances
    key_passes = df['key_passes'] / appearances
    duels_ratio = df['duels_ratio']
    dribble_ratio = df['dribble_ratio']
    cross_ratio = df['cross_ratio']

    # Goalkeepers Rating
    if (df['position_id'] == 1):
        weighted_rating = (saves_ratio * 100) + (clean_sheets_ratio * 200) + (penalties_saved_ratio * 15) + \
            (df['pass_accuracy'] * 10) + \
            (yellow_cards_ratio * -50) + (red_cards_ratio * -100) + \
            (fouls_committed_ratio * -50)

    # Defenders Rating
    elif (df['position_id'] == 2):
        weighted_rating = (tackles_ratio * 1000) + (clean_sheets_ratio * 600) + (total_passes_ratio * 20) + (
            yellow_cards_ratio * -50) + (red_cards_ratio * -100) + (duels_ratio * 2) + (fouls_committed_ratio * -30)

    # Midfielders Rating
    elif (df['position_id'] == 3):
        weighted_rating = (goals_ratio * 90) + (assists_ratio * 110) + (total_passes_ratio * 7) + (
            df['pass_accuracy'] * 10) + (yellow_cards_ratio * -50) + (red_cards_ratio * -100) + (dribble_ratio * 50) + (cross_ratio * 25) + (fouls_committed_ratio * -50)

    # Strikers/Wingers Rating
    elif (df['position_id'] == 4):
        weighted_rating = (goals_ratio * 110) + (assists_ratio * 100) + (total_passes_ratio * 5) + (
            df['pass_accuracy'] * 10) + (yellow_cards_ratio * -50) + (red_cards_ratio * -100) + (dribble_ratio * 25) + (cross_ratio * 50) + (fouls_committed_ratio * -50)

    final_rating = round((weighted_rating / 100), 2)
    print(final_rating)
    return final_rating


# playerRating(580) # Cristiano Ronaldo
# playerRating(184798) # Lionel Messi
# playerRating(184941) # Sergio Ramos
# playerRating(30594) # Alex Sandro
# playerRating(186029) # Keylor Navas
# playerRating(1743) # Virgil van Dijk
# playerRating(30642) # Maneul Neuer
