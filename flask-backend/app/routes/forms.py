from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import DataRequired, URL


class PokemonForm(FlaskForm):
    number = IntegerField("Number", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    attack = IntegerField("Attack", validators=[DataRequired()])
    defense = IntegerField("Number", validators=[DataRequired()])
    imageUrl = StringField("Image Url", validators=[DataRequired()])
    type = StringField("Type", validators=[DataRequired()])
    moves = StringField("Moves", validators=[DataRequired()])
    encounterRate = IntegerField("Encounter Rate", validators=[DataRequired()])
    catchRate = IntegerField("Catch Rate", validators=[DataRequired()])
    captured = BooleanField("Captured", validators=[DataRequired()])


class ItemForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    happiness = IntegerField("Image Url", validators=[DataRequired()])
    price = IntegerField("Image Url", validators=[DataRequired()])
