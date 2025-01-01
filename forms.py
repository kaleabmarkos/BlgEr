from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

'''
Data Validators from wtforms.validators:
DataRequired - The value can't be empty
Length - sets a required length for the input
Email - Email Validator
EqualTo - checks if 2 given inputs are equal
StringField - datatype - string
PassWordField - Type for passwords
BooleanField - Boolean Field
'''

class Registeration(FlaskForm):
    user_name = StringField("Username: ", 
                            validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField("Email: ", validators=[DataRequired(), Email()])
    password = PasswordField("Password: ", validators=[DataRequired()])
    conf_password = PasswordField("Confirm Password: ", 
                              validators=[DataRequired(), EqualTo("password")])
    
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField("Email: ", validators=[DataRequired(), Email()])
    password = PasswordField("Password: ", validators=[DataRequired()])
    remember_me = BooleanField("Remember",validators=[DataRequired()])
    submit = SubmitField("Login")