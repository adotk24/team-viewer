from .db import db, environment, SCHEMA, add_prefix_for_prod

class Player(db.Model):
    __tablename__ =  'players'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}


    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(50),  nullable=False)
    lastName = db.Column(db.String(50), nullable=False)
    height = db.Column(db.Integer, nullable=False)
    number = db.Column(db.Integer, nullable=False)
    teamId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('teams.id')) ,nullable=False)
    year = db.Column(db.String(10))
    position = db.Column(db.String(50), nullable=False)

    teams = db.relationship('Team', back_populates='players', cascade='all, delete')
    stats = db.relationship('Stat', back_populates='players')

    def to_dict(self):
        return {
            'id' : self.id,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'height' : self.height,
            'number': self.number,
            'teamId': self.teamId,
            'year': self.year,
            'position': self.position
        }
