from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError

from app.domain.shared.user import User

class LoginForm(Form):

    email = StringField('Email', validators=[Required(message="This field is required."), Length(1, 64), Email(message="Please enter a valid email.")])
    password = PasswordField('Password', validators=[Required(message="This field is required.")])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')
