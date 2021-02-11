from django.db import models

# Create your models here.


class Player(models.Model):
    player_id = models.IntegerField()
    player_name = models.CharField(max_length=200)
    image_path = models.URLField()
    nationality = models.CharField(max_length=200)
    clicks = models.IntegerField(default=0)

    def __str__(self):
        return self.player_name


class Search(models.Model):
    searchquery = models.CharField(max_length=200)

    def __str__(self):
        return self.searchquery
