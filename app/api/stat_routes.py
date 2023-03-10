from flask import Flask, jsonify, Blueprint, redirect, request
from ..models import db, Team, Game, Player, Stat
from flask_login import login_required, current_user
from ..forms import StatForm
stat_route = Blueprint('stats', __name__)


#Get All Stats for Specific Game
@stat_route.route('/team/<int:gameId>')
def get_stats_by_game(gameId):
    response = []
    score1 = 0
    score2 = 0
    stats = Stat.query.filter_by(gameid = gameId).all()
    team1id = None
    team2id = None
    if not stats:
        return jsonify({'Stats': None,
                        'scores': None})
    for stat in stats:
        if team1id == None:
            team1id = stat.teamid
        elif team1id != None and stat.teamid != team1id:
            team2id = stat.teamid
        if (stat.teamid == team1id):
            score1 += stat.points
        elif (stat.teamid == team2id):
            score2 += stat.points
        if team2id == None:
            team2id = 0
        player = Player.query.filter_by(id = stat.playerid).first().to_dict()
        team = Team.query.filter_by(id = stat.teamid).first().to_dict()
        response.append({
            'id': stat.id,
            'teamid': stat.teamid,
            'team': team,
            'playerid': stat.playerid,
            'player': player,
            'gameid': stat.gameid,
            'points': stat.points,
            'rebounds': stat.rebounds,
            'assists': stat.assists
        })
    return jsonify({'Stats': response,
                    "scores": {team1id : score1,
                               team2id : score2}
                    })


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

#Add Stat to Game by Player
@stat_route.route('/<int:gameId>/<int:teamId>/<int:playerId>/add', methods=['POST'])
def add_stat(gameId, teamId, playerId):
    form = StatForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    response = []
    form['teamid'].data = teamId
    form['gameid'].data = gameId
    form['playerid'].data = playerId

    if form.validate_on_submit():
        new_stat = Stat(
            teamid = teamId,
            playerid = playerId,
            gameid = gameId,
            points = form.data['points'],
            rebounds = form.data['rebounds'],
            assists = form.data['assists']
        )
        response.append(new_stat.to_dict())
    if form.errors:
        print('*********************************************************', form.errors)
        return 'Invalid data'
    db.session.add(new_stat)
    db.session.commit()
    return jsonify({'Stat': response})

#EDIT A STAT
@stat_route.route('/<int:gameId>/<int:teamId>/<int:playerId>/<int:statId>/edit', methods=['PUT'])
def edit_stat(gameId, teamId, playerId, statId):
    stat = Stat.query.filter_by(id = statId).first()
    form = StatForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    form['teamid'].data = teamId
    form['gameid'].data = gameId
    form['playerid'].data = playerId
    if form.validate_on_submit():
        setattr(stat, "points", form.data['points'])
        setattr(stat, 'rebounds', form.data['rebounds'])
        setattr(stat, 'assists', form.data['assists'])
        setattr(stat, 'teamid', teamId)
        setattr(stat, 'gameid', gameId)
        setattr(stat, 'playerid', playerId)
    if form.errors:
        return 'Invalid Data'
    db.session.commit()
    return stat.to_dict()

@stat_route.route('/<int:statId>/delete', methods=['DELETE'])
def delete_stat(statId):
    stat = Stat.query.filter_by(id = statId).first()
    if not stat:
        return 'No Stat Found'
    else:
        db.session.delete(stat)
        db.session.commit()
        return {'message': "Successfully Deleted", 'statusCode': 200}
