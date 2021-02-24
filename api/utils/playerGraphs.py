import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from .aws import memory_to_aws
import io

plt.rcParams["font.family"] = "Avenir"


def attackersGraph(df, player_id):
    appearances = df['appearances']
    goals_ratio = df['goals'] / appearances
    assists_ratio = df['assists'] / appearances
    key_passes_ratio = df['key_passes'] / appearances
    successful_dribbles_ratio = df['successful_dribbles'] / appearances
    successful_crosses_ratio = df['successful_crosses'] / appearances

    plt.switch_backend('Agg')
    fig = plt.figure(figsize=(5, 3))  # added figsize
    ax = fig.add_subplot(1, 1, 1)
    x = np.linspace(0, appearances + 200, 50)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    below = x <= appearances
    above = x > appearances - 40
    y = goals_ratio*x
    plt.plot(x[below], y[below], '-r', label='Goals', markevery=10)
    plt.plot(x[above], y[above], '--r',  markevery=10)
    y = assists_ratio*x
    plt.plot(x[below], y[below], '-g', label='Assists')
    plt.plot(x[above], y[above], '--g')
    y = key_passes_ratio*x
    plt.plot(x[below], y[below], '-b', label='Key Passes')
    plt.plot(x[above], y[above], '--b')
    y = successful_dribbles_ratio*x
    plt.plot(x[below], y[below], '-m', label='Dribbles')
    plt.plot(x[above], y[above], '--m')
    y = successful_crosses_ratio*x
    plt.plot(x[below], y[below], '-c', label='Crosses')
    plt.plot(x[above], y[above], '--c')
    plt.xlabel('Appearances')
    plt.ylabel('Statistics')
    plt.legend(loc='upper left')
    ax.set_facecolor('aliceblue')
    plt.tight_layout()
    img_data = io.BytesIO()
    plt.savefig(img_data, format='png')
    img_data.seek(0)
    memory_to_aws(img_data, '%s.png' % player_id)
    return 'https://socceranalyzer.s3.us-east-2.amazonaws.com/%s.png' % player_id


def defendersGraph(df, player_id):
    appearances = df['appearances']
    tackles_ratio = df['tackles'] / appearances
    clean_sheets_ratio = df['clean_sheets'] / appearances
    successful_duels_ratio = df['successful_duels'] / appearances
    fouls_committed_ratio = df['fouls_committed'] / appearances

    plt.switch_backend('Agg')
    fig = plt.figure(figsize=(5, 3))
    ax = fig.add_subplot(1, 1, 1)
    x = np.linspace(0, appearances + 200, 50)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    below = x <= appearances
    above = x > appearances - 40
    y = tackles_ratio*x
    plt.plot(x[below], y[below], '-r', label='Tackles', markevery=10)
    plt.plot(x[above], y[above], '--r',  markevery=10)
    y = clean_sheets_ratio*x
    plt.plot(x[below], y[below], '-g', label='Clean Sheets')
    plt.plot(x[above], y[above], '--g')
    y = successful_duels_ratio*x
    plt.plot(x[below], y[below], '-b', label='Duels')
    plt.plot(x[above], y[above], '--b')
    y = fouls_committed_ratio*x
    plt.plot(x[below], y[below], '-m', label='Fouls Committed')
    plt.plot(x[above], y[above], '--m')
    plt.xlabel('Appearances')
    plt.ylabel('Statistics')
    plt.legend(loc='upper left')
    ax.set_facecolor('aliceblue')
    plt.tight_layout()
    img_data = io.BytesIO()
    plt.savefig(img_data, format='png')
    img_data.seek(0)
    memory_to_aws(img_data, '%s.png' % player_id)
    return 'https://socceranalyzer.s3.us-east-2.amazonaws.com/%s.png' % player_id


def keepersGraph(df, player_id):
    appearances = df['appearances']
    saves_ratio = df['saves'] / appearances
    clean_sheets_ratio = df['clean_sheets'] / appearances
    penalties_saved_ratio = df['penalties_saved'] / appearances

    plt.switch_backend('Agg')
    fig = plt.figure(figsize=(5, 3))
    ax = fig.add_subplot(1, 1, 1)
    x = np.linspace(0, appearances + 200, 50)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    below = x <= appearances
    above = x > appearances - 40
    y = saves_ratio*x
    plt.plot(x[below], y[below], '-r', label='Saves', markevery=10)
    plt.plot(x[above], y[above], '--r',  markevery=10)
    y = clean_sheets_ratio*x
    plt.plot(x[below], y[below], '-g', label='Clean Sheets')
    plt.plot(x[above], y[above], '--g')
    y = penalties_saved_ratio*x
    plt.plot(x[below], y[below], '-b', label='Penalties Saved')
    plt.plot(x[above], y[above], '--b')
    plt.xlabel('Appearances')
    plt.ylabel('Statistics')
    plt.legend(loc='upper left')
    ax.set_facecolor('aliceblue')
    plt.tight_layout()
    img_data = io.BytesIO()
    plt.savefig(img_data, format='png')
    img_data.seek(0)
    memory_to_aws(img_data, '%s.png' % player_id)
    return 'https://socceranalyzer.s3.us-east-2.amazonaws.com/%s.png' % player_id


def playerGraphs(df, player_id):

    # Goalkeepers Rating
    if (df['position_id'] == 1):
        return keepersGraph(df, player_id)

    # Defenders Rating
    elif (df['position_id'] == 2):
        return defendersGraph(df, player_id)

    elif (df['position_id'] == 3):
        return attackersGraph(df, player_id)

    # Strikers/Wingers Rating
    elif (df['position_id'] == 4):
        return attackersGraph(df, player_id)


# playerGraphs(580)  # Cristiano Ronaldo
# playerGraphs(184798)  # Lionel Messi
# playerGraphs(184941)  # Sergio Ramos
# playerGraphs(30594)  # Alex Sandro
# playerGraphs(186029)  # Keylor Navas
