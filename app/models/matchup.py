from .db import db, environment, SCHEMA, add_prefix_for_prod



# matchup = db.Table(
#     'matchup',
#     db.Column('team1id', db.Integer, db.ForeignKey(add_prefix_for_prod('teams.id'), primary_key=True)),
#     db.Column('team2id', db.Integer, db.ForeignKey(add_prefix_for_prod('teams.id'), primary_key=True))
# )

class Matchup(db.Model):
    __tablename__ ='matchup'
    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}
    id = db.Column(db.Integer, primary_key=True)
    team1id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('teams.id')))
    team2id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('teams.id')))
