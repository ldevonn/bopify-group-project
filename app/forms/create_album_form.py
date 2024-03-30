from flask_wtf import FlaskForm
from wtforms.fields import StringField, DateField, SelectField, SubmitField
from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms.validators import DataRequired
from app.api.aws import ALLOWED_IMG_EXTENSIONS

GENRES = [
    "Rock",
    "Pop",
    "Hip hop",
    "Jazz",
    "Blues",
    "Electronic",
    "Folk",
    "R&B",
    "Country",
    "Soul",
    "Funk",
    "Reggae",
    "Latin",
    "Classical",
    "Electronic dance music (EDM)",
    "Heavy metal",
    "Alternative",
    "Indie",
    "Punk",
    "Grunge",
    "Country",
    "Metal",
    "Alternative",
    "Ska",
    "Reggae",
    "Salsa",
    "Afrobeat",
    "Flamenco",
    "Bossa nova",
    "Trance",
    "House",
    "Techno",
    "Drum and bass",
    "Dubstep",
    "Trap",
    "Jungle",
    "Glitch",
    "Psychedelic"
]

ALBUM_TYPES = ["Album", "Single"]

class CreateAlbumForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    releaseDate = DateField("Release Date", validators=[DataRequired()], format="%m/%d/%Y")
    albumType = SelectField("Album Type", choices=ALBUM_TYPES, validators=[DataRequired()])
    genre = SelectField("Genre", choices=GENRES, validators=[DataRequired()])
    imageUrl = FileField("Album Image", validators=[FileRequired(), FileAllowed(list(ALLOWED_IMG_EXTENSIONS))])
    submit = SubmitField("Submit")
