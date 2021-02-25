from rest_framework import serializers
from .models import Player, Team, TeamH2HStats, TeamH2HFixtures


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class TeamH2HStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamH2HStats
        fields = '__all__'

class TeamH2HFixturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamH2HFixtures
        fields = '__all__'
