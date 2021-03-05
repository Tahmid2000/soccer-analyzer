from django.db import models

# Create your models here.

# for all players: player_id, team_id, country_id, position_id, display_name, nationality, birthdate, height, weight, image_path
# regular players: apperances, goals, assists, interceptions, yellowcards, yellowred + redcards, tackles, fouls comitted, total passes, accuracy on passes
# goalie: appearances, saves, cleansheets, penalities saved


class Player(models.Model):
    player_id = models.IntegerField()  # initial data
    player_name = models.CharField(max_length=200)  # initial data
    image_path = models.URLField()  # initial data
    nationality = models.CharField(max_length=200)  # initial data
    clicks = models.IntegerField(default=0)  # initial data
    team_id = models.IntegerField(default=None, blank=True, null=True)
    team_name = models.CharField(
        default=None, blank=True, null=True, max_length=200)
    country_id = models.IntegerField(default=None, blank=True, null=True)
    position_id = models.IntegerField(default=None, blank=True, null=True)
    player_rating = models.FloatField(default=None, blank=True, null=True)
    position = models.CharField(
        max_length=200, default=None, blank=True, null=True)
    birthdate = models.DateField(default=None, blank=True, null=True)
    height = models.IntegerField(default=None, blank=True, null=True)
    weight = models.IntegerField(default=None, blank=True, null=True)
    appearances = models.IntegerField(default=None, blank=True, null=True)
    goals = models.IntegerField(default=None, blank=True, null=True)
    assists = models.IntegerField(default=None, blank=True, null=True)
    yellow_cards = models.IntegerField(default=None, blank=True, null=True)
    red_cards = models.IntegerField(default=None, blank=True, null=True)
    tackles = models.IntegerField(default=None, blank=True, null=True)
    fouls_committed = models.IntegerField(default=None, blank=True, null=True)
    total_passes = models.IntegerField(default=None, blank=True, null=True)
    pass_accuracy = models.FloatField(default=None, blank=True, null=True)
    saves = models.IntegerField(default=None, blank=True, null=True)
    clean_sheets = models.IntegerField(default=None, blank=True, null=True)
    penalties_saved = models.IntegerField(default=None, blank=True, null=True)
    dribble_ratio = models.FloatField(default=None, blank=True, null=True)
    successful_dribbles = models.IntegerField(
        default=None, blank=True, null=True)
    cross_ratio = models.FloatField(default=None, blank=True, null=True)
    successful_crosses = models.IntegerField(
        default=None, blank=True, null=True)
    duels_ratio = models.FloatField(default=None, blank=True, null=True)
    successful_duels = models.IntegerField(
        default=None, blank=True, null=True)
    key_passes = models.IntegerField(default=None, blank=True, null=True)
    graph_path = models.URLField(default=None, blank=True, null=True)
    last_updated = models.DateTimeField(
        default=None, blank=True, null=True)  # initial data

    def __str__(self):
        return self.player_name


class Search(models.Model):
    searchquery = models.CharField(max_length=200)

    def __str__(self):
        return self.searchquery


class SearchTeam(models.Model):
    searchquery = models.CharField(max_length=200)

    def __str__(self):
        return self.searchquery


class Team(models.Model):
    team_id = models.IntegerField(default=None, blank=True, null=True)
    team_name = models.CharField(
        max_length=200, default=None, blank=True, null=True)
    image_path = models.URLField(default=None, blank=True, null=True)
    # initial data
    clicks = models.IntegerField(default=0,  blank=True, null=True)
    founded = models.CharField(
        max_length=200, default=None, blank=True, null=True)
    country = models.CharField(
        max_length=200, default=None, blank=True, null=True)
    venue_name = models.CharField(
        max_length=200, default=None, blank=True, null=True)


class TeamH2HStats(models.Model):
    id1 = models.IntegerField(default=None, blank=True, null=True)
    id2 = models.IntegerField(default=None, blank=True, null=True)
    total_games = models.IntegerField(default=None, blank=True, null=True)
    home_id1_games = models.IntegerField(default=None, blank=True, null=True)
    away_id1_games = models.IntegerField(default=None, blank=True, null=True)
    home_id1_wins = models.IntegerField(default=None, blank=True, null=True)
    away_id1_wins = models.IntegerField(default=None, blank=True, null=True)
    home_id1_draws = models.IntegerField(default=None, blank=True, null=True)
    away_id1_draws = models.IntegerField(default=None, blank=True, null=True)
    home_id1_losses = models.IntegerField(default=None, blank=True, null=True)
    away_id1_losses = models.IntegerField(default=None, blank=True, null=True)
    home_id1_goals_for = models.IntegerField(
        default=None, blank=True, null=True)
    home_id1_goals_against = models.IntegerField(
        default=None, blank=True, null=True)
    away_id1_goals_for = models.IntegerField(
        default=None, blank=True, null=True)
    away_id1_goals_against = models.IntegerField(
        default=None, blank=True, null=True)
    home_id2_games = models.IntegerField(default=None, blank=True, null=True)
    away_id2_games = models.IntegerField(default=None, blank=True, null=True)
    home_id2_wins = models.IntegerField(default=None, blank=True, null=True)
    away_id2_wins = models.IntegerField(default=None, blank=True, null=True)
    home_id2_draws = models.IntegerField(default=None, blank=True, null=True)
    away_id2_draws = models.IntegerField(default=None, blank=True, null=True)
    home_id2_losses = models.IntegerField(default=None, blank=True, null=True)
    away_id2_losses = models.IntegerField(default=None, blank=True, null=True)
    home_id2_goals_for = models.IntegerField(
        default=None, blank=True, null=True)
    home_id2_goals_against = models.IntegerField(
        default=None, blank=True, null=True)
    away_id2_goals_for = models.IntegerField(
        default=None, blank=True, null=True)
    away_id2_goals_against = models.IntegerField(
        default=None, blank=True, null=True)
    id1_graph_path = models.URLField(default=None, blank=True, null=True)
    id2_graph_path = models.URLField(default=None, blank=True, null=True)
    total_graph_path = models.URLField(default=None, blank=True, null=True)
    last_updated = models.DateTimeField(
        default=None, blank=True, null=True)


class TeamH2HFixtures(models.Model):
    id1 = models.IntegerField(default=None, blank=True, null=True)
    id2 = models.IntegerField(default=None, blank=True, null=True)
    league = models.CharField(
        max_length=200, default=None, blank=True, null=True)
    date = models.DateTimeField(default=None, blank=True, null=True)
    fixture_round = models.CharField(max_length=200, default=None, blank=True, null=True)
    status = models.CharField(
        max_length=200, default=None, blank=True, null=True)
    venue = models.CharField(
        max_length=200, default=None, blank=True, null=True)
    home_logo = models.URLField(default=None, blank=True, null=True)
    away_logo = models.URLField(default=None, blank=True, null=True)
    score = models.CharField(
        max_length=200, default=None, blank=True, null=True)
    last_updated = models.DateTimeField(
        default=None, blank=True, null=True)
