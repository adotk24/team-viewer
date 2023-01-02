from flask import Flask, jsonify, Blueprint, redirect, request
from ..models import db, Team, Game
from flask_login import login_required, current_user
from ..forms import GameForm
game_route = Blueprint('games', __name__)
from datetime import datetime


#Get All Games
@game_route.route('/')
def get_all_games():
    response = []
    games = Game.query.all()
    for game in games:
        response.append({
            'id': game.id,
            'datetime': game.datetime,
            'team1id': game.team1id
        })
    return jsonify({'Games': response})

#Get Single Game
@game_route.route('/<int:gameId>')
def get_single_game(gameId):
    game = Game.query.get(gameId)
    return game.to_dict()

# Create a Game
@game_route.route('/add', methods=['POST'])
def create_game():
    form = GameForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    schedule = (form.data['year'], form.data['month'], form.data['day'], form.data['hour'], form.data['minute'])
    if form.validate_on_submit():
        new_game = Game(
            datetime = datetime(int(str((schedule)))),
            team1id = form.data['team1id']
        )
    if form.errors:
        print('**********************************', form.errors, schedule)
        return 'Invalid data'
    db.session.add(new_game)
    db.session.commit()
    return new_game.to_dict()
