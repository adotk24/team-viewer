from flask import Flask, jsonify, Blueprint, redirect, request
from ..models import db, Player
from flask_login import login_required, current_user
from ..forms import PlayerForm
player_route = Blueprint('players', __name__)


#Get Player By ID
@player_route.route('/player/<int:playerId>')
def get_player_by_id(playerId):
    player = Player.query.get(playerId)
    return player.to_dict()

#Get All Players by Team ID
@player_route.route('/<int:teamId>')
def get_players_by_team(teamId):
    players = Player.query.filter_by(teamId = teamId).order_by(Player.number.asc()).all()
    response = []
    for player in players:
        response.append({
            'id' : player.id,
            'firstName': player.firstName,
            'lastName': player.lastName,
            'height' : player.height,
            'number': player.number,
            'teamId': player.teamId,
            'year': player.year,
            'position': player.position
        })
    return jsonify({'Players': response})

#Create Player w TeamId
@player_route.route('/<int:teamId>/add', methods=['POST'])
def create_player(teamId):
    form = PlayerForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        new_player = Player(
            firstName = form.data['firstName'],
            lastName = form.data['lastName'],
            height = form.data['height'],
            number = form.data['number'],
            year = form.data['year'],
            position = form.data['position'],
            teamId = teamId
        )
    if form.errors:
        return 'Invalid Data'

    db.session.add(new_player)
    db.session.commit()

    return new_player.to_dict()

#Edit Player w TeamId
@player_route.route('/<int:teamId>/<int:playerId>/edit', methods = ['PUT'])
def edit_player(teamId, playerId):
    player = Player.query.filter_by(id = playerId).first()
    form = PlayerForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        setattr(player, 'firstName', form.data['firstName'])
        setattr(player, 'lastName', form.data['lastName'])
        setattr(player, 'height', form.data['height'])
        setattr(player, 'number', form.data['number'])
        setattr(player, 'year', form.data['year'])
        setattr(player, 'position', form.data['position'])
        setattr(player, 'teamId', teamId)
    if form.errors:
        return 'Invalid Data'
    db.session.commit()
    return player.to_dict()

#Delete Player
@player_route.route('/player/<int:playerId>/delete', methods = ['DELETE'])
def delete_player(playerId):
    player = Player.query.filter_by(id = playerId).first()
    if not player:
        return 'No Player Found!'
    else:
        db.session.delete(player)
        db.session.commit()
        return {"message": "Successfully Deleted!", "statusCode": 200}
