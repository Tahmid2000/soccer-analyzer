import pandas as pd
from playerInfo import *
import matplotlib.pyplot as plt
import numpy as np


def playerGraphs(player_id):

    df = getPlayerInfo(player_id)

    appearances = df['appearances']
    goals_ratio = df['goals'] / appearances
    assists_ratio = df['assists'] / appearances
    key_passes_ratio = df['key_passes'] / appearances
    successful_dribbles_ratio = df['successful_dribbles'] / appearances
    successful_crosses_ratio = df['successful_crosses'] / appearances

    player_dataframe = [goals_ratio, assists_ratio, key_passes_ratio, successful_dribbles_ratio, successful_crosses_ratio]
    index = ['Goals', 'Assists', 'Key Passes', 'Successful Dribbles', 'Successful Crosses']

    charts_df = pd.DataFrame(player_dataframe, index=index)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    x = np.linspace(0,appearances + 200,50)

    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    markers_on = [100, 200, 500, 1000]
    plt.plot(x, goals_ratio*x, '-r.', label='Goals', markevery=10)
    plt.plot(x, assists_ratio*x,'-g', label='Assists')
    plt.plot(x, key_passes_ratio*x,'-b', label='Key Passes')
    plt.plot(x, successful_dribbles_ratio*x,'-m', label='Dribbles')
    plt.plot(x, successful_crosses_ratio*x,'-c', label='Crosses')

    plt.xlabel('Appearances')
    plt.ylabel('Statistics')
    plt.legend(loc='upper left')
    ax.set_facecolor('aliceblue')
    plt.show()


    # Goalkeepers Rating
    if (df['position_id'] == 1):
        pass

    # Defenders Rating
    elif (df['position_id'] == 2):
        pass

    elif (df['position_id'] == 3):
        pass

    # Strikers/Wingers Rating
    # Goal ratio, assist ratio, successful dribbles ratio, successful crosses ratio, total passes ratio
    elif (df['position_id'] == 4):
        pass        


playerGraphs(580) # Cristiano Ronaldo
# playerGraphs(184798) # Lionel Messi
# playerGraphs(184941) # Sergio Ramos
# playerGraphs(30594) # Alex Sandro
# playerGraphs(186029) # Keylor Navas
