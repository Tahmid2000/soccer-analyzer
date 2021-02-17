import pandas as pd
from playerInfo import *


def playerRating(player_id):

    df = getPlayerInfo(player_id)
    print(df)

    # Goalkeepers Rating
    if (df['position_id'] == 1):
        weighted_rating = (df['saves'] * 1) + (df['clean_sheets'] * 5) + (df['appearances'] * 0.05) + (df['total_passes'] * 0.015) + (df['yellow_cards'] * -0.5) + (df['red_cards'] * -0.8) +  (df['penalties_saved'] * 0.3)
   
    # Defenders Rating
    elif (df['position_id'] == 2):
        weighted_rating = (df['goals'] * 1) + (df['assists'] * 0.5) + (df['appearances'] * 0.05) + (df['total_passes'] * 0.015) + (df['yellow_cards'] * -0.5) + (df['red_cards'] * -0.8) +  (df['tackles'] * 0.3)
    
    # Midfielders Rating
    elif (df['position_id'] == 3):
        weighted_rating = (df['goals'] * 1) + (df['assists'] * 0.5) + (df['appearances'] * 0.05) + (df['total_passes'] * 0.015) + (df['yellow_cards'] * -0.5) + (df['red_cards'] * -0.8) +  (df['tackles'] * 0.3)
    
    # Strikers/Wingers Rating
    elif (df['position_id'] == 4):
        weighted_rating = (df['goals'] * 1) + (df['assists'] * 0.5) + (df['appearances'] * 0.05) + (df['total_passes'] * 0.015) + (df['yellow_cards'] * -0.5) + (df['red_cards'] * -0.8) +  (df['tackles'] * 0.3)
    
    print(weighted_rating)

    

# playerRating(580) # Cristiano Ronaldo
playerRating(184798) # Lionel Messi
# playerRating(184941) # Sergio Ramos
# playerRating(30594) # Alex Sandro
# playerRating(186029) # Keylor Navas

