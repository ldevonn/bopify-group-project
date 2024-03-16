from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import (DataRequired, Email, ValidationError)
from app.models import Playlist, Track


# def user_exists(form, field):
#     # Checking if user exists
#     email = field.data
#     user = User.query.filter(User.email == email).first()
#     if user:
#         raise ValidationError('Email address is already in use.')


# def username_exists(form, field):
#     # Checking if username is already in use
#     username = field.data
#     user = User.query.filter(User.username == username).first()
#     if user:
#         raise ValidationError('Username is already in use.')


class PlaylistForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    image_url = StringField('image')
