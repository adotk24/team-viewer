from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime
from sqlalchemy import ForeignKey

class Game(db.Model):
    __tablename__ = 'games'
    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(), nullable=False)
    time = db.Column(db.DateTime())
    team1id = db.Column(db.Integer, ForeignKey('teams.id'))
    team2id = db.Column(db.Integer, ForeignKey('teams.id'))

    teams = db.relationship('Team', back_populates='games')
    team1 = db.relationship('Team', foreign_keys=[teams.id])
    team2 = db.relationship('Team', foreign_keys=[teams.id])

    def to_dict(self):
        return {
            'id' : self.id,
            'date': self.date,
            'time': self.time,
            'team1id': self.team1id,
            'team2id' : self.team2id
        }
