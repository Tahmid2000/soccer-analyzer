import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from .teamH2H import teamsInfo

plt.rcParams["font.family"] = "Avenir"


def totalGraphs(df, id1, id2, team1, team2):
    fig1, axs = plt.subplots(2, 1, figsize=(8, 8))

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
    plt.show()


def team1Graphs(df, id1, id2, team1, team2):
    fig1, axs = plt.subplots(2, 1, figsize=(5, 5))

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
    plt.show()


def team2Graphs(df, id1, id2, team1, team2):
    fig1, axs = plt.subplots(2, 1, figsize=(5, 5))

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
    plt.show()


def teamGraphs(id1, id2, team1, team2):
    df = teamsInfo(id1, id2)['stats']
    totalGraphs(df, id1, id2, team1, team2)
    team1Graphs(df, id1, id2, team1, team2)
    team2Graphs(df, id1, id2, team1, team2)


""" teamGraphs(40, 50, 'Liverpool', 'Manchester United') """
