from wtforms import StringField, PasswordField, SubmitField, TextAreaField, RadioField
from flask_wtf import FlaskForm, RecaptchaField
from wtforms.validators import DataRequired, EqualTo
from flask_wtf.file import FileField, FileAllowed

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('Password',
                             validators=[DataRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Confirm Password')
    recaptcha = RecaptchaField()
    submit = SubmitField('Sign Me Up')

class RequestPasswordReset(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField('Send Password Reset Link')

class PasswordReset(FlaskForm):
    password = PasswordField('New Password',
                             validators=[DataRequired(), EqualTo('confirm', message='Passwords must match')])
    recaptcha = RecaptchaField()
    confirm = PasswordField('Confirm Password')
    submit = SubmitField('Reset Password')


class ResendConfirmation(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField('Resend Confirmation link')

class NewReview(FlaskForm):
    submit = SubmitField('Add New Review')

class EditReview(FlaskForm):
    edit_button = SubmitField('Save Edit')
    delete_button = SubmitField('Delete Review (Cannot be Undone)')

class PictureForm(FlaskForm):
    picture = FileField('Browse Files', validators=[FileAllowed(upload_set=['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Submit Avatar')

class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log Me In')

class ReviewForm(FlaskForm):
    rating = RadioField('rating', choices=[("5", "str5"), ("4", "str4"), ("3", "str3"), ("2", "str2"), ("1", "str1")],
                        validators=[DataRequired()])
    text = TextAreaField('Written Review')
    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')


