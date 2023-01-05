from flask_wtf import FlaskForm
from wtforms.fields import (
    StringField, SubmitField, IntegerField, DateTimeField
)
from wtforms.validators import DataRequired
from datetime import datetime

dr = [DataRequired()]
class GameForm(FlaskForm):
    year = IntegerField('Year', dr)
    month = IntegerField('Month', dr)
    day = IntegerField('Day', dr)
    hour = IntegerField('Hour', dr)
    minute = IntegerField('Minute')
    team1id = IntegerField('Team 1 Id', dr)
    team2id = IntegerField('Team 2 Id', dr)
