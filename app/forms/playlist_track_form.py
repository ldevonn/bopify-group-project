from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

class PlaylistTrackForm(FlaskForm):
    track_id = IntegerField('Track ID', validators=[DataRequired()])
    submit = SubmitField('Add Track to Playlist')