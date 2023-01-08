from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime
from sqlalchemy import ForeignKey

class Game(db.Model):
    __tablename__ = 'games'
    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime(), nullable=False)
    # matchupId = db.Column(db.Integer, nullable=False)
    team1id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('teams.id')))
    team2id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('teams.id')))
    stats = db.relationship('Stat', back_populates='games', cascade='all, delete')


    # team1_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('teams.id')))
    # team2_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('teams.id')))
    # teams = db.relationship('Team', back_populates='games', lazy='selectin',
    # primaryjoin="or_(Team.id==Game.team1id, " "Team.id==Game.team2id)")

    # teams = db.relationship('Team', foreign_keys=('Game.team1id'))
    # teams = db.relationship('Team', foreign_keys=('Game.team2id'))
    # team1 = db.relationship('Team', foreign_keys=[team1_id])
    # team2 = db.relationship('Team', foreign_keys=[team2_id])


    # team1 = db.relationship('Team', back_populates='games')
    # team2 = db.relationship('Team', back_populates='games')

    # team1 = db.relationship('Team', foreign_keys=('Game.team1id'))
    # team2 = db.relationship('Team', foreign_keys=('Game.team2id'))

    # team1 = db.relationship('Team', foreign_keys=[teams.id], backref='team1id', lazy=True)
    # team2 = db.relationship('Team', foreign_keys=[teams.id], backref='team2id', lazy=True)
    # db.Column('team1id', db.Integer, db.ForeignKey('teams.id'))
    # db.Column('team2id', db.Integer, db.ForeignKey('teams.id'))

    def to_dict(self):
        return {
            'id' : self.id,
            'datetime': self.datetime,
            'team1id': self.team1id,
            'team2id' : self.team2id
            # 'matchupId' : self.matchupId
        }
