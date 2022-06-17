from flask_wtf import FlaskForm
from wtforms import (
    StringField, TextAreaField, SubmitField, validators,
    ValidationError)
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
    name = StringField(
      'Name', validators=[DataRequired(
        "Please enter your name.")])
    email = StringField(
      'Email', validators=[DataRequired(
        "Please enter your email address."), Email(granular_message=True)])
    subject = StringField(
      'Subject', validators=[DataRequired(
        "Please enter a subject.")])
    message = TextAreaField(
      'Message', validators=[DataRequired(
        "Please enter a message.")])
    submit = SubmitField("Send")
