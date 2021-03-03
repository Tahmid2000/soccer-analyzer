from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils.playerName import getPlayers
from .utils.playerInfo import getPlayerInfo, getTeam
from .utils.playerRating import playerRating
from .utils.playerGraphs import playerGraphs
from .utils.teamGraphs import teamGraphs
from .utils.teamName import getTeams
from .utils.teamH2H import teamsInfo
from .serializers import *
from .models import *
from django.db.models import Q, F
from django.utils.timezone import utc, now
import datetime


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Players': '/players/<str:pk>/',
        'PlayerStats': 'player/stats/<int:id>',
        'Teams': '/teams/<str:pk>/',
        'TeamH2H': 'teams/h2h/<int:id1>/<int:id2>'
    }
    return Response(api_urls)


@api_view(['GET'])
def players(request, pk):
    if len(pk) < 4:
        return Response(None)
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
    player1 = Player.objects.filter(player_id=id).first()
    timediff = 0
    if player1.last_updated:
        now_time = now()
        timediff = (now_time - player1.last_updated).days
    if not player1.last_updated or timediff >= 2:
        stats = getPlayerInfo(id)
        team_name = getTeam(stats['team_id'])
        player1_rating = playerRating(stats)
        player1_graph = playerGraphs(stats, id)
        Player.objects.filter(player_id=id).update(player_rating=player1_rating, team_id=stats['team_id'], team_name=team_name, country_id=stats['country_id'], position=stats['position'], birthdate=stats['birthdate'], height=stats['height'], weight=stats['weight'], appearances=stats['appearances'], goals=stats['goals'], assists=stats['assists'], yellow_cards=stats['yellow_cards'],
                                                   red_cards=stats['red_cards'], tackles=stats['tackles'], fouls_committed=stats['fouls_committed'], total_passes=stats['total_passes'], pass_accuracy=stats['pass_accuracy'], saves=stats['saves'], clean_sheets=stats['clean_sheets'], penalties_saved=stats['penalties_saved'], dribble_ratio=stats['dribble_ratio'], successful_dribbles=stats['successful_dribbles'], cross_ratio=stats['cross_ratio'], successful_crosses=stats['successful_crosses'], duels_ratio=stats['duels_ratio'], successful_duels=stats['successful_duels'], key_passes=stats['key_passes'], graph_path=player1_graph, last_updated=now())
    Player.objects.filter(player_id=id).update(clicks=F('clicks') + 1)
    player = Player.objects.filter(player_id=id).first()
    serializer = PlayerSerializer(player)
    return Response(serializer.data)


@api_view(['GET'])
def teams(request, pk):
    if len(pk) < 4:
        return Response(None)
    searches = SearchTeam.objects.filter(searchquery=pk.lower()).count()
    if searches == 0:
        newTeams = getTeams(pk.lower())
        for team in newTeams:
            num = Team.objects.filter(team_id=team['team_id']).count()
            if num == 0:
                newTeam = Team(team_id=team['team_id'], team_name=team['team_name'],
                               image_path=team['image_path'], founded=team['founded'], country=team['country'], venue_name=team['venue_name'], clicks=0)
                newTeam.save()
        search = SearchTeam(searchquery=pk.lower())
        search.save()
    teams = Team.objects.filter(
        Q(team_name__icontains=pk.lower())).order_by('-clicks')[:50]
    serializer = TeamSerializer(teams, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def teamsH2H(request, id1, id2):
    teamStats = TeamH2HStats.objects.filter(id1=id1, id2=id2).first()
    teamFixtures = TeamH2HFixtures.objects.filter(id1=id1, id2=id2)
    Team.objects.filter(team_id=id1).update(clicks=F('clicks') + 1)
    Team.objects.filter(team_id=id2).update(clicks=F('clicks') + 1)
    team1 = Team.objects.filter(team_id=id1).first()
    team2 = Team.objects.filter(team_id=id2).first()
    timediff = 0
    if teamStats:
        now_time = now()
        timediff = (now_time - teamStats.last_updated).days
    if not teamStats or timediff >= 2:
        data = teamsInfo(id1, id2)
        stats = data['stats']
        fixtures = data['fixtures']
        team_graphs = teamGraphs(
            stats, id1, id1, team1.team_name, team2.team_name)
        if TeamH2HStats.objects.filter(id1=id1, id2=id2).count() == 0:
            statsSaved = TeamH2HStats(id1=id1, id2=id2, total_games=stats['total_games'], home_id1_games=stats['home_id1_games'], away_id1_games=stats['away_id1_games'], home_id1_wins=stats['home_id1_wins'], away_id1_wins=stats['away_id1_wins'], home_id1_draws=stats['home_id1_draws'], away_id1_draws=stats['away_id1_draws'], home_id1_losses=stats['home_id1_losses'], away_id1_losses=stats['away_id1_losses'], home_id1_goals_for=stats['home_id1_goals_for'], home_id1_goals_against=stats['home_id1_goals_against'], away_id1_goals_for=stats['away_id1_goals_for'], away_id1_goals_against=stats['away_id1_goals_against'], home_id2_games=stats['home_id2_games'],
                                      away_id2_games=stats['away_id2_games'], home_id2_wins=stats['home_id2_wins'], away_id2_wins=stats['away_id2_wins'], home_id2_draws=stats['home_id2_draws'], away_id2_draws=stats['away_id2_draws'], home_id2_losses=stats['home_id2_losses'], away_id2_losses=stats['away_id2_losses'], home_id2_goals_for=stats['home_id2_goals_for'], home_id2_goals_against=stats['home_id2_goals_against'], away_id2_goals_for=stats['away_id2_goals_for'], away_id2_goals_against=stats['away_id2_goals_against'], id1_graph_path=team_graphs['team1'], id2_graph_path=team_graphs['team2'], total_graph_path=team_graphs['total'], last_updated=now())
            statsSaved.save()
        else:
            TeamH2HStats.objects.filter(id1=id1, id2=id2).update(id1=id1, id2=id2, total_games=stats['total_games'], home_id1_games=stats['home_id1_games'], away_id1_games=stats['away_id1_games'], home_id1_wins=stats['home_id1_wins'], away_id1_wins=stats['away_id1_wins'], home_id1_draws=stats['home_id1_draws'], away_id1_draws=stats['away_id1_draws'], home_id1_losses=stats['home_id1_losses'], away_id1_losses=stats['away_id1_losses'], home_id1_goals_for=stats['home_id1_goals_for'], home_id1_goals_against=stats['home_id1_goals_against'], away_id1_goals_for=stats['away_id1_goals_for'], away_id1_goals_against=stats['away_id1_goals_against'], home_id2_games=stats[
                'home_id2_games'], away_id2_games=stats['away_id2_games'], home_id2_wins=stats['home_id2_wins'], away_id2_wins=stats['away_id2_wins'], home_id2_draws=stats['home_id2_draws'], away_id2_draws=stats['away_id2_draws'], home_id2_losses=stats['home_id2_losses'], away_id2_losses=stats['away_id2_losses'], home_id2_goals_for=stats['home_id2_goals_for'], home_id2_goals_against=stats['home_id2_goals_against'], away_id2_goals_for=stats['away_id2_goals_for'], away_id2_goals_against=stats['away_id2_goals_against'], id1_graph_path=team_graphs['team1'], id2_graph_path=team_graphs['team2'], total_graph_path=team_graphs['total'], last_updated=now())
        difference = len(fixtures) - \
            TeamH2HFixtures.objects.filter(id1=id1, id2=id2).count()
        if difference > 0:
            for fixture in fixtures[-1*difference:]:
                fixtureSaved = TeamH2HFixtures(id1=id1, id2=id2, league=fixture['league'], date=fixture['date'], fixture_round=fixture['round'], status=fixture['status'],
                                               venue=fixture['venue'], home_logo=fixture['home_logo'], away_logo=fixture['away_logo'], score=fixture['score'], last_updated=now())
                fixtureSaved.save()
    returnStatistics = TeamH2HStats.objects.filter(id1=id1, id2=id2).first()
    returnFixtures = TeamH2HFixtures.objects.filter(id1=id1, id2=id2)
    serializerTeam1 = TeamSerializer(team1)
    serializerTeam2 = TeamSerializer(team2)
    serializerStatistics = TeamH2HStatsSerializer(returnStatistics)
    serializerFixtures = TeamH2HFixturesSerializer(returnFixtures, many=True)
    serializerList = {'team1': serializerTeam1.data, 'team2': serializerTeam2.data,
                      'stats': serializerStatistics.data, 'fixtures': serializerFixtures.data}
    content = {'data': serializerList}
    return Response(content)
