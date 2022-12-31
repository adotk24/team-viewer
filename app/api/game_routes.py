from flask import Flask, jsonify, Blueprint, redirect, request
from ..models import db, Game
from flask_login import login_required, current_user
# from ..forms import GameForm
game_route = Blueprint('games', __name__)
