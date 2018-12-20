from wtforms import StringField, PasswordField, SubmitField, TextAreaField, RadioField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, EqualTo, InputRequired

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('Password',
                             validators=[DataRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Confirm Password')
    submit = SubmitField('Sign Me Up')

class NewReview(FlaskForm):
    submit = SubmitField('Add New Review')

class EditReview(FlaskForm):
    submit = SubmitField('Save Edit')

class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log Me In')

class ReviewForm(FlaskForm):
    rating = RadioField('rating', choices=[("5", "str5"), ("4", "str4"), ("3", "str3"), ("2", "str2"), ("1", "str1")],
                        validators=[InputRequired(message='Please choose a rating')])
    text = TextAreaField('Written Review')
    submit = SubmitField('Submit')


