from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email
import email_validator

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired('Name is required')])
    email = StringField('Email', validators=[DataRequired('A valid email is required'), Email()])
    subject = StringField('Subject', validators=[DataRequired('Subject is required'), Length(min = 5, max = 15)])
    message = TextAreaField('Message', validators=[DataRequired('Message is required'), Length(min  = 5, max = 500)])
    sendMsg = SubmitField('Send Message')