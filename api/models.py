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
    country_id = models.IntegerField(default=None, blank=True, null=True)
    position_id = models.IntegerField(default=None, blank=True, null=True)
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
    pass_accuracy = models.IntegerField(default=None, blank=True, null=True)
    saves = models.IntegerField(default=None, blank=True, null=True)
    clean_sheets = models.IntegerField(default=None, blank=True, null=True)
    penalties_saved = models.IntegerField(default=None, blank=True, null=True)
    last_updated = models.DateTimeField(
        default=None, blank=True, null=True)  # initial data

    def __str__(self):
        return self.player_name


class Search(models.Model):
    searchquery = models.CharField(max_length=200)

    def __str__(self):
        return self.searchquery
