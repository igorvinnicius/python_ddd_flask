from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError

from app.domain.shared.user import User

class RegisterForm(Form):

    name = StringField('Name', validators=[Required(), Length(1, 64)])
    email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[Required()])
    password = PasswordField('Password', validators=[Required(), EqualTo('password_confirm', message='Passwords must match.')])
    password_confirm = PasswordField('Confirm password', validators=[Required()])
    submit = SubmitField('Register')

    def get_user(self):
        return User(name = self.name.data, email = self.email.data, password = self.password.data)
