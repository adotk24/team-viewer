from .db import db, environment, SCHEMA, add_prefix_for_prod



matchup = db.Table(
    'matchup',
    db.Column('team1id', db.Integer, db.ForeignKey(add_prefix_for_prod('teams.id'), primary_key=True)),
    db.Column('team2id', db.Integer, db.ForeignKey(add_prefix_for_prod('teams.id'), primary_key=True))
)

if environment == 'production':
    follows.schema = SCHEMA
