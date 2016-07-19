from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import login_user, logout_user

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app

from app.infrastructure.repositories.user_repository import UserRepository

user_repository = UserRepository()

class AuthenticationService(object):

    @staticmethod
    def generate_hash(password):
        return generate_password_hash(password)

    @staticmethod
    def check_password(hash, password):
        return check_password_hash(hash, password)

    @staticmethod
    def login(email, password):

        user = user_repository.get_by_email(email=email)

        print email
        if user is not None and AuthenticationService.check_password(user.password_hash, password):
            login_user(user, remember=True)

    @staticmethod
    def logout_current_user():
        logout_user()

    @staticmethod
    def get_current_user(self):
        return user_repository.get_by_email(flask.ext.login.current_user.email)

    @staticmethod
    def register(user):
        user.password_hash = AuthenticationService.generate_hash(user.password)
        user_repository.create(user)

    @staticmethod
    def generate_confirmation_account_token(user_id, expiration=3600):
        serializer = Serializer(current_app.config['SECRET_KEY'], expiration)
        return serializer.dumps({'confirm': user_id})

    @staticmethod
    def confirm_user_account(token):

        serializer = Serializer(current_app.config['SECRET_KEY'])

        try:
            data = serializer.loads(token)
        except:
            return False

        user = user_repository.get_by_id(data.get('confirm'))

        if user is None:
            return False

        user.confirmed = True
        user_repository.save(user)
        return True
