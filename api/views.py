from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils.playerName import getPlayers
from .serializers import PlayerSerializer
from .models import Player, Search
from django.db.models import Q


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Players': '/players/<str:pk>/'
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
        Q(player_name__icontains=pk.lower())).order_by('clicks')[:50]
    serializer = PlayerSerializer(players, many=True)
    return Response(serializer.data)
