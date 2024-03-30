from flask_wtf import FlaskForm
from wtforms.fields import StringField, IntegerField, SubmitField, SelectField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired
from app.api.aws import ALLOWED_MUSIC_EXTENSIONS

class EditTrackForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    duration = IntegerField("Duration", validators=[DataRequired()])
    albumId = SelectField("Album Id", validators=[DataRequired()], coerce=int)
    submit = SubmitField("Submit")
