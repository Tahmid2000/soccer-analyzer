from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class SearchPlayerForm(FlaskForm):
    name = StringField('Lastname', validators=[
                       DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Search')


class SearchTeamForm(FlaskForm):
    name = StringField('Teamname', validators=[
                       DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Search')
