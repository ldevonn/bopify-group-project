from flask_wtf import FlaskForm
from wtforms.fields import StringField, IntegerField, SubmitField, SelectField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired
from app.api.aws import ALLOWED_MUSIC_EXTENSIONS

class TrackForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    duration = IntegerField("Duration", validators=[DataRequired()])
    file = FileField("Music File", validators=[FileRequired(), FileAllowed(list(ALLOWED_MUSIC_EXTENSIONS))])
    albumId = SelectField("Album Id", validators=[DataRequired()], coerce=int)
    submit = SubmitField("Submit")
