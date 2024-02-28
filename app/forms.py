# Relevant Imports
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Email

class ContactForm(FlaskForm):
    # String Fields
    user_name = StringField('Name', validators=[InputRequired()])
    user_email = StringField('E-mail', validators=[InputRequired(), Email()])
    mail_subject = StringField('Subject', validators=[InputRequired()])

    # Text Fields
    message = TextAreaField('Message', validators=[InputRequired()])

    # Submission Field
    submit = SubmitField('Submit')