from .db import db, environment, SCHEMA, add_prefix_for_prod

class Stat(db.Model):
    __tablename__ = 'stats'
    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    teamid = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('teams.id')))
    playerid = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('players.id')))
    gameid = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('games.id')))
    points = db.Column(db.Integer)
    rebounds = db.Column(db.Integer)
    assists = db.Column(db.Integer)

    teams = db.relationship('Team', back_populates='stats')
    players = db.relationship('Player', back_populates='stats')
    games = db.relationship('Game', back_populates='stats')
    def to_dict(self):
        return {
            'id' : self.id,
            'teamid': self.teamid,
            'playerid': self.playerid,
            'gameid' : self.gameid,
            'points' : self.points,
            'rebounds' : self.rebounds,
            'assists' : self.assists
        }
