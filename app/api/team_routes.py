from flask import Flask, jsonify, Blueprint, redirect, request
from ..models import db, Team, User
from flask_login import login_required, current_user
from ..forms import TeamForm
team_route = Blueprint('teams', __name__)

#Get All Teams

@team_route.route('/')
def get_all_teams():
    response = []
    teams = Team.query.all()
    for team in teams:
        response.append({
            "id": team.id,
            "name": team.name,
            "mascot": team.mascot,
            'city': team.city,
            'state': team.state,
            'year': team.year
        })
    return jsonify({'Teams': response})

#Get ALL user Teams
@team_route.route('/user')
def get_all_user_teams():
    response = []
    teams = Team.query.filter_by(userId = current_user.id).all()
    user = User.query.filter_by(id = current_user.id).first()
    for team in teams:
        response.append({
            'id': team.id,
            'name': team.name,
            'mascot' : team.mascot,
            'city' : team.city,
            'state' : team.state,
            'year' : team.year,
            'userId': team.userId
        })

    return jsonify({'Teams': response})


#Get SINGLE team

@team_route.route('/<int:teamId>')
def get_single_team(teamId):
    team = Team.query.get(teamId)
    response = []
    response.append({
        'id': team.id,
        'name': team.name,
        'mascot': team.mascot,
        'city': team.city,
        'state': team.state,
        'year' : team.year,
        'userId': team.userId
    })
    return jsonify(response)

# Create Team
@team_route.route('/add', methods=['POST'])
def create_team():
    form = TeamForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        new_team = Team(
            name = form.data['name'],
            mascot = form.data['mascot'],
            city = form.data['city'],
            state = form.data['state'],
            year = form.data['year']
        )
    if form.errors:
        return "Invalid data"

    db.session.add(new_team)
    db.session.commit()

    return new_team.to_dict()

# Edit a Team
@team_route.route('/<int:teamId>/edit', methods=['PUT'])
def edit_team(teamId):
    team = Team.query.filter_by(id = teamId).first()
    form = TeamForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        setattr(team, 'name', form.data['name'])
        setattr(team, 'mascot', form.data['mascot'])
        setattr(team, 'city', form.data['city'])
        setattr(team, 'state', form.data['state'])
        setattr(team, 'year', form.data['year'])
    if form.errors:
        return 'Invalid data'
    db.session.commit()
    return team.to_dict()

# Delete a Team
@team_route.route('/<int:teamId>', methods=['DELETE'])
def delete_team(teamId):
    team = Team.query.filter_by(id = teamId).first()
    if not team:
        return ('No Team Found')
    else:
        db.session.delete(team)
        db.session.commit()
        return {"message": "Successfully Deleted!", "statusCode": 200}
