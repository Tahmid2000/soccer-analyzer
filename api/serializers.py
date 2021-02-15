from rest_framework import serializers
from .models import Player


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['player_id', 'player_name', 'image_path', 'nationality', 'clicks', 'team_id', 'country_id', 'position_id', 'birthdate', 'height', 'weight', 'appearances',
                  'goals', 'assists', 'yellow_cards', 'red_cards', 'tackles', 'fouls_committed', 'total_passes', 'pass_accuracy', 'saves', 'clean_sheets', 'penalties_saved', 'last_updated']
