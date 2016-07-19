import os
basedir = os.path.abspath(os.path.dirname(__file__))

from app.context import *

class Config:

	CONTEXT_FACTORY = Context
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	SQLALCHEMY_RECORD_QUERIES = True
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	SYSTEM_MAIL_SUBJECT_PREFIX = '[ADMIN]'
	SYSTEM_MAIL_SENDER = 'Admin <>'
	SYSTEM_ADMIN = os.environ.get('SYSTEM_ADMIN')


	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')



config = {

    'default': DevelopmentConfig
}
