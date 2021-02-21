from rest_framework import serializers
from .models import Player


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['player_id', 'player_name', 'image_path', 'nationality', 'clicks', 'team_id', 'country_id', 'position', 'birthdate', 'height', 'weight', 'player_rating', 'appearances',
                  'goals', 'assists', 'yellow_cards', 'red_cards', 'tackles', 'fouls_committed', 'total_passes', 'pass_accuracy', 'saves', 'clean_sheets', 'penalties_saved', 'dribble_ratio', 'successful_dribbles', 'cross_ratio', 'successful_crosses', 'duels_ratio', 'successful_duels', 'key_passes', 'graph_path', 'last_updated']
