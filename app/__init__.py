from flask import Flask
from config import config
from context import Context

from injector import inject
from flask_injector import FlaskInjector

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail

from flask.ext.assets import Environment

from .assets import bundles

db = SQLAlchemy()

context = Context(db)
mail = Mail()
login_manager = LoginManager()
login_manager.user_loader(context.user_repository.get_by_id)
login_manager.session_protection = 'strong'
login_manager.login_view = 'shared.login'


def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)
	mail.init_app(app)
	login_manager.setup_app(app)

	assets = Environment(app)
	assets.register(bundles())

	from .shared import shared as shared_blueprint
	app.register_blueprint(shared_blueprint)

	from .admin import admin as admin_blueprint
	app.register_blueprint(admin_blueprint)

	from .blog import blog as blog_blueprint
	app.register_blueprint(blog_blueprint)

	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	db.init_app(app)

	# with app.app_context():
	# # Extensions like Flask-SQLAlchemy now know what the "current" app
	# # is while within this block. Therefore, you can now run........
	# 	db.create_all()

	return app
