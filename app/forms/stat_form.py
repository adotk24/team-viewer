from flask_wtf import FlaskForm
from wtforms.fields import (
    StringField, SubmitField, IntegerField, DateTimeField
)
from wtforms.validators import DataRequired

dr =[DataRequired()]

class StatForm(FlaskForm):
    points = IntegerField('Points', dr)
    rebounds = IntegerField('Rebounds', dr)
    assists = IntegerField('Assists', dr)
    teamid = IntegerField('Team ID', dr)
    playerid = IntegerField('Player ID', dr)
    gameid = IntegerField('Game ID', dr)
