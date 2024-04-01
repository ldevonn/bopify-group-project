from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import User
from flask_wtf.file import FileAllowed, FileField, FileRequired
from app.api.aws import ALLOWED_IMG_EXTENSIONS


def user_exists(form, field):
    # Checking if user exists
    email = field.data
    print("<-------------------------------------------------->")
    print("EMAIL: ", email)
    print("<-------------------------------------------------->")
    user = User.query.filter(User.email == email).first()
    print("<-------------------------------------------------->")
    print("<-------------------------------------------------->")
    print("USER: ", user)
    print("<-------------------------------------------------->")
    print("<-------------------------------------------------->")
    if user:
        print("HIT!!!!!!!!!!!!!!!!!!!")
        raise ValidationError('Email address is already in use.')


# def username_exists(form, field):
#     # Checking if username is already in use
#     username = field.data
#     user = User.query.filter(User.username == username).first()
#     if user:
#         raise ValidationError('Username is already in use.')


class SignUpForm(FlaskForm):
    # username = StringField(
    #     'username', validators=[DataRequired(), username_exists])
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), user_exists])
    password = StringField('Password', validators=[DataRequired()])
    image_url = FileField("Profile Picture", validators=[FileRequired(), FileAllowed(list(ALLOWED_IMG_EXTENSIONS))])
    is_artist = BooleanField('Are you an artist?')
