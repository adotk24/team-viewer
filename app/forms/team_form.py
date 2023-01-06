from flask_wtf import FlaskForm
from wtforms.fields import (
    StringField, SubmitField, IntegerField
)
from wtforms.validators import DataRequired
dr = [DataRequired()]

class TeamForm(FlaskForm):
    name = StringField('Name', dr)
    mascot = StringField('Mascot', dr)
    city = StringField('City', dr)
    state = StringField ('State', dr)
