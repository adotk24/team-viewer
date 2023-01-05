from flask import Flask, jsonify, Blueprint, redirect, request
from ..models import db, Team, Game, Matchup, Player
from flask_login import login_required, current_user
from ..forms import GameForm
game_route = Blueprint('games', __name__)
from datetime import datetime


#Get All Games for Specific Team
@game_route.route('/team/<int:teamId>')
def get_all_games_team(teamId):
    response = []
    games = Game.query.all()
    for game in games:
        team1 = Team.query.filter_by(id = game.team1id).first().to_dict()
        team2 = Team.query.filter_by(id = game.team2id).first().to_dict()
        if team1["id"] == teamId or team2["id"] == teamId:
            response.append({
                'id': game.id,
                'datetime': game.datetime,
                'team1': team1,
                'team2': team2
        })
    return jsonify({'Games': response})

#Get All Games for Specific Player
# @game_route.route('/player/<int:playerId>')
# def get_all_games_player(playerId):
#     response = []
#     games = Game.query.all()
#     player = Player.query.filter_by(id = playerId).first()
#     for game in games:
#         matchup = Matchup.query.filter_by(id = game.matchupId).first()
#         team1 = Team.query.filter_by(id = matchup.team1id).first().to_dict()
#         team2 = Team.query.filter_by(id = matchup.team2id).first().to_dict()
#         if team1["id"] == player.teamId or team2["id"] == player.teamId:
#             response.append({
#                 'id': game.id,
#                 'datetime': game.datetime,
#                 'team1': team1,
#                 'team2': team2
#             })


#Get Single Game
@game_route.route('/<int:gameId>')
def get_single_game(gameId):
    game = Game.query.get(gameId)
    team1 = Team.query.filter_by(id = game.team1id).first().to_dict()
    team2 = Team.query.filter_by(id = game.team2id).first().to_dict()
    response = []
    response.append({
        'id': game.id,
        'datetime': game.datetime,
        'team1': team1,
        'team2': team2
    })
    return jsonify({'Game': response})


# Create a Game
@game_route.route('/add', methods=['POST'])
def create_game():
    form = GameForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    matchup = Matchup.query.filter_by(id = form.data['matchupId']).first()
    team1 = Team.query.filter_by(id = matchup.team1id).first().to_dict()
    team2 = Team.query.filter_by(id = matchup.team2id).first().to_dict()
    response = []
    if form.validate_on_submit():
        new_game = Game(
            datetime = datetime(form.data['year'], form.data['month'], form.data['day'], form.data['hour'], form.data['minute']),
            matchupId = form.data['matchupId']
        )
    print('******************************************************', team1, team2)
    response.append(new_game.to_dict())
    response.append(team1)
    response.append(team2)
    if form.errors:
        return 'Invalid data'
    db.session.add(new_game)
    db.session.commit()
    return jsonify({'Game': response})

# Edit a Game
@game_route.route('/<int:gameId>/edit', methods=['PUT'])
def edit_game(gameId):
    game = Game.query.get(gameId)
    form = GameForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    response = []
    if form.validate_on_submit():
        setattr(game, 'datetime', datetime(form.data['year'], form.data['month'], form.data['day'], form.data['hour'], form.data['minute']))
        setattr(game, 'matchupId', form.data['matchupId'])
    if form.errors:
        return 'Invalid data'
    response.append(game.to_dict())
    matchup = Matchup.query.filter_by(id = form.data['matchupId']).first()
    team1 = Team.query.filter_by(id = matchup.team1id).first().to_dict()
    team2 = Team.query.filter_by(id = matchup.team2id).first().to_dict()
    response.append(team1)
    response.append(team2)
    db.session.commit()
    return jsonify({'Game': response})

# Delete a Game
@game_route.route('/<int:gameId>/delete', methods=['DELETE'])
def delete_game(gameId):
    game = Game.query.get(gameId)
    if not game:
        return 'No Game Found'
    else:
        db.session.delete(game)
        db.session.commit()
        return {"message": "Successfully Deleted!", 'statusCode': 200 }
