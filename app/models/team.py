from .db import db, environment, SCHEMA, add_prefix_for_prod
# from .matchup import matchup
class Team(db.Model):
    __tablename__ = 'teams'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    mascot = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')))

    players = db.relationship('Player', back_populates='teams', cascade='all, delete')
    users = db.relationship('User', back_populates='teams')
    stats = db.relationship('Stat', back_populates='teams', cascade='all, delete')
    games = db.relationship("Game", primaryjoin="or_(Game.team1id == Team.id, Game.team2id == Team.id)", back_populates="teams", cascade='all, delete')

    def to_dict(self):
        return {
            'id' : self.id,
            'name': self.name,
            'mascot' : self.mascot,
            'city' : self.city,
            'state' : self.state,
            'userId': self.userId
        }
