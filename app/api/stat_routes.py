from flask import Flask, jsonify, Blueprint, redirect, request
from ..models import db, Team, Game, Player, Stat
from flask_login import login_required, current_user
# from ..forms import StatForm
stat_route = Blueprint('stats', __name__)


#Get All Stats for Specific Game
@stat_route.route('/team/<int:gameId>')
def get_stats_by_game(gameId):
    response = []
    stats = Stat.query.filter_by(gameid = gameId).all()
    for stat in stats:
        response.append({
            'id': stat.id,
            'teamid': stat.teamid,
            'playerid': stat.playerid,
            'gameid': stat.gameid,
            'points': stat.points,
            'rebounds': stat.rebounds,
            'assists': stat.assists
        })

    return jsonify({'Stats': response})


#Get All Stats by Player
@stat_route.route('/player/<int:playerId>')
def get_stats_by_player(playerId):
    response = []
    stats = Stat.query.filter_by(playerid = playerId).all()
    for stat in stats:
        response.append({
            'id': stat.id,
            'teamid': stat.teamid,
            'playerid': stat.playerid,
            'gameid': stat.gameid,
            'points': stat.points,
            'rebounds': stat.rebounds,
            'assists': stat.assists
        })

    return jsonify({'Stats': response})
