from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils.playerName import getPlayers
from .utils.playerInfo import getPlayerInfo
from .serializers import PlayerSerializer
from .models import Player, Search
from django.db.models import Q, F
from django.utils.timezone import utc
import datetime


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Players': '/players/<str:pk>/',
        'PlayerStats': 'player/stats/<int:id>'
    }
    return Response(api_urls)


@api_view(['GET'])
def players(request, pk):
    searches = Search.objects.filter(searchquery=pk.lower()).count()
    if searches == 0:
        newplayers = getPlayers(pk.lower())
        for player in newplayers:
            num = Player.objects.filter(player_id=player['player_id']).count()
            if num == 0:
                newplayer = Player(player_id=player['player_id'], player_name=player['player_name'],
                                   image_path=player['image_path'], nationality=player['nationality'], clicks=0)
                newplayer.save()
        search = Search(searchquery=pk.lower())
        search.save()
    players = Player.objects.filter(
        Q(player_name__icontains=pk.lower())).order_by('-clicks')[:50]
    serializer = PlayerSerializer(players, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def playerStats(request, id):
    # return Response(getPlayerInfo(id))
    player1 = Player.objects.filter(player_id=id).first()
    timediff = 0
    if player1.last_updated:
        now = datetime.datetime.utcnow().replace(tzinfo=utc)
        timediff = (now - player1.last_updated).days
    if not player1.last_updated or timediff >= 2:  #
        stats = getPlayerInfo(id)
        Player.objects.filter(player_id=id).update(team_id=stats['team_id'], country_id=stats['country_id'], position=stats['position'], birthdate=stats['birthdate'], height=stats['height'], weight=stats['weight'], appearances=stats['appearances'], goals=stats['goals'], assists=stats['assists'], yellow_cards=stats['yellow_cards'],
                                                   red_cards=stats['red_cards'], tackles=stats['tackles'], fouls_committed=stats['fouls_committed'], total_passes=stats['total_passes'], pass_accuracy=stats['pass_accuracy'], saves=stats['saves'], clean_sheets=stats['clean_sheets'], penalties_saved=stats['penalties_saved'], dribble_ratio=stats['dribble_ratio'], successful_dribbles=stats['successful_dribbles'], cross_ratio=stats['cross_ratio'], successful_crosses=stats['successful_crosses'], duels_ratio=stats['duels_ratio'], successful_duels=stats['successful_duels'], key_passes=stats['key_passes'], last_updated=datetime.datetime.now())
    Player.objects.filter(player_id=id).update(clicks=F('clicks') + 1)
    player = Player.objects.filter(player_id=id).first()
    serializer = PlayerSerializer(player)
    return Response(serializer.data)
