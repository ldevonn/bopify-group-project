from flask_wtf import FlaskForm
from wtforms.fields import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired

class TrackForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    duration = IntegerField("Duration", validators=[DataRequired()])
    file = StringField("File", validators=[DataRequired()])
    albumId = SelectField("Album Id", validators=[DataRequired()], coerce=int)
    submit = SubmitField("Submit")