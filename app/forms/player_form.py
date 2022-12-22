from flask_wtf import FlaskForm
from wtforms.fields import (
    StringField, SubmitField, IntegerField
)
from wtforms.validators import DataRequired
dr = [DataRequired()]

class PlayerForm(FlaskForm):
    firstName = StringField('First Name', dr)
    lastName = StringField('Last Name', dr)
    height = IntegerField('Height', dr)
    number = IntegerField('Number', dr)
    year = StringField('Year', dr)
    position = StringField('Position', dr)
