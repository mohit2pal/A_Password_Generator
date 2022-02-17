from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class SignUpForm(FlaskForm):
    name = StringField("Enter your Name")
    age = StringField("Enter your age")
    passion = StringField("Enter the Application/Website name")
    master_password = StringField("Enter the Master Password")
    submit = SubmitField("Submit")
