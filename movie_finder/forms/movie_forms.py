from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SubmitField, FloatField


class ADDMovieForm(FlaskForm):
    title = StringField()
    description = TextAreaField("Description")
    duration = FloatField("duration")
    image = FileField("Cover")
    submit = SubmitField("Add")


