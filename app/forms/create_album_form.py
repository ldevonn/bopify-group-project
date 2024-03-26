from flask_wtf import FlaskForm
from wtforms.fields import StringField, DateField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

# def validate_album(form, field):
#     if

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
    imageUrl = StringField("Image Url", validators=[DataRequired()])
    submit = SubmitField("Submit")
