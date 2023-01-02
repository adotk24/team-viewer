from .db import db, environment, SCHEMA, add_prefix_for_prod

class Team(db.Model):
    __tablename__ = 'teams'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    mascot = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer)
    userId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')))

    players = db.relationship('Player', back_populates='teams', cascade='all, delete')
    users = db.relationship('User', back_populates='teams')
    games = db.relationship('Game', back_populates='teams', cascade='all, delete')

    def to_dict(self):
        return {
            'id' : self.id,
            'name': self.name,
            'mascot' : self.mascot,
            'city' : self.city,
            'state' : self.state,
            'year' : self.year,
            'userId': self.userId
        }
