import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from .teamH2H import teamsInfo
from .aws import memory_to_aws
import io

plt.rcParams["font.family"] = "Avenir"
plt.rcParams["font.size"] = "22"


def totalGraphs(df, id1, id2, team1, team2):
    fig1, axs = plt.subplots(2, 1, figsize=(11, 11))

    labels1 = '%s Home' % team1, '%s Away' % team1, '%s Home' % team2, '%s Away' % team2, '%s Home Draws' % team1, '%s Home Draws' % team2
    sizes1 = [df['home_id1_wins'], df['away_id1_wins'],
              df['home_id2_wins'], df['away_id2_wins'], df['home_id1_draws'], df['away_id1_draws']]
    axs[0].set_title('Game Win %')
    axs[0].pie(sizes1, labels=labels1, autopct='%1.1f%%',
               shadow=True, startangle=90)
    axs[0].axis('equal')
    axs[0].set_facecolor('aliceblue')

    labels2 = '%s Home' % team1, '%s Away' % team1, '%s Home' % team2, '%s Away' % team2
    sizes2 = [df['home_id1_goals_for'], df['away_id1_goals_for'],
              df['home_id2_goals_for'], df['away_id2_goals_for']]

    axs[1].set_title('Goals For %')
    axs[1].pie(sizes2, labels=labels2, autopct='%1.1f%%',
               shadow=True, startangle=90)

    axs[1].axis('equal')
    axs[1].set_facecolor('aliceblue')
    plt.tight_layout()

    img_data = io.BytesIO()
    plt.savefig(img_data, format='png')
    img_data.seek(0)
    memory_to_aws(img_data, '%svs%stotal.png' % id1, id2)
    return 'https://socceranalyzer.s3.us-east-2.amazonaws.com/%svs%stotal.png' % id1, id2


def team1Graphs(df, id1, id2, team1, team2):
    fig1, axs = plt.subplots(2, 1, figsize=(10, 7))

    labels1 = team1, team2, 'Draws'
    sizes1 = [df['home_id1_wins'], df['away_id2_wins'], df['home_id1_draws']]
    axs[0].set_title('Games at %s' % team1)
    axs[0].pie(sizes1, labels=labels1, autopct='%1.1f%%',
               shadow=True, startangle=90)
    axs[0].axis('equal')
    axs[0].set_facecolor('aliceblue')

    labels2 = team1, team2
    sizes2 = [df['home_id1_goals_for'], df['away_id2_goals_for']]

    axs[1].set_title('Goals at %s' % team1)
    axs[1].pie(sizes2, labels=labels2, autopct='%1.1f%%',
               shadow=True, startangle=90)

    axs[1].axis('equal')
    axs[1].set_facecolor('aliceblue')
    plt.tight_layout()

    img_data = io.BytesIO()
    plt.savefig(img_data, format='png')
    img_data.seek(0)
    memory_to_aws(img_data, '%svs%shome.png' % id1, id2)
    return 'https://socceranalyzer.s3.us-east-2.amazonaws.com/%svs%shome.png' % id1, id2


def team2Graphs(df, id1, id2, team1, team2):
    fig1, axs = plt.subplots(2, 1, figsize=(10, 7))

    labels1 = team2, team1, 'Draws'
    sizes1 = [df['home_id2_wins'], df['away_id1_wins'], df['home_id2_draws']]
    axs[0].set_title('Games at %s' % team2)
    axs[0].pie(sizes1, labels=labels1, autopct='%1.1f%%',
               shadow=True, startangle=90)
    axs[0].axis('equal')
    axs[0].set_facecolor('aliceblue')

    labels2 = team2, team1
    sizes2 = [df['home_id2_goals_for'], df['away_id1_goals_for']]

    axs[1].set_title('Goals at %s' % team2)
    axs[1].pie(sizes2, labels=labels2, autopct='%1.1f%%',
               shadow=True, startangle=90)

    axs[1].axis('equal')
    axs[1].set_facecolor('aliceblue')
    plt.tight_layout()

    img_data = io.BytesIO()
    plt.savefig(img_data, format='png')
    img_data.seek(0)
    memory_to_aws(img_data, '%svs%saway.png' % id1, id2)
    return 'https://socceranalyzer.s3.us-east-2.amazonaws.com/%svs%saway.png' % id1, id2


def teamGraphs(stats, id1, id2, team1, team2):
    #stats = teamsInfo(id1, id2)['stats']
    return {'total': totalGraphs(stats, id1, id2, team1, team2), 'team1': team1Graphs(stats, id1, id2, team1, team2), 'team2': team2Graphs(stats, id1, id2, team1, team2)}


""" teamGraphs(40, 50, 'Liverpool', 'Manchester United') """
