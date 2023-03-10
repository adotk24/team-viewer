from flask.cli import AppGroup
from .users import seed_users, undo_users
from .team import seed_teams, undo_teams
from app.models.db import db, environment, SCHEMA
from .player import seed_players, undo_players
from .game import seed_games, undo_games
from .stat import seed_stats, undo_stats
# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo
        # command, which will  truncate all tables prefixed with
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_users()
        undo_teams()
        undo_players()
        undo_games()
        undo_stats()
    seed_users()
    seed_teams()
    seed_players()
    seed_games()
    seed_stats()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_teams()
    undo_players()
    undo_games()
    undo_stats()
    # Add other undo functions here
