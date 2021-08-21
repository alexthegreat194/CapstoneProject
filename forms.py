from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField("Username:", validators=[DataRequired()])
    password = StringField("Password:", validators=[DataRequired()])
    submit = SubmitField("Submit")

class CreateAccountForm(FlaskForm):
    username = StringField("Username:", validators=[DataRequired()])
    password = StringField("Password:", validators=[DataRequired()])
    submit = SubmitField("Submit")

class EditAccountForm(FlaskForm):
    discord = StringField("Discord:", validators=[DataRequired()])
    description = StringField("Description:", validators=[DataRequired()])
    submit = SubmitField("Submit")

class CreateItem(FlaskForm):
    name = StringField("Name:", validators=[DataRequired()])
    price = StringField("Price:", validators=[DataRequired()])
    image = StringField("Image Name:", validators=[DataRequired()])
    submit = SubmitField("Submit")