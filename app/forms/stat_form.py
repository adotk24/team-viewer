from flask_wtf import FlaskForm
from wtforms.fields import (
    StringField, SubmitField, IntegerField, DateTimeField
)
from wtforms.validators import DataRequired

dr =[DataRequired()]

class StatForm(FlaskForm):
    points = IntegerField('Points')
    rebounds = IntegerField('Rebounds')
    assists = IntegerField('Assists')
    teamid = IntegerField('Team ID', dr)
    playerid = IntegerField('Player ID', dr)
    gameid = IntegerField('Game ID', dr)
