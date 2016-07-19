import os
from app import create_app
from flask.ext.script import Manager, Shell
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

def make_shell_context():
    return dict(app=app, db=db)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

@manager.command
def tests():
	"""Run the unit tests."""
	import unittest
	tests = unittest.TestLoader().discover('app.domain.tests.services')
	unittest.TextTestRunner(verbosity=2).run(tests)

@manager.command
def db_setup():
	from app import context
	db = SQLAlchemy(app)
	context.setup(db)

@manager.command
def setup_user_roles():
	from app import context
	from flask.ext.sqlalchemy import SQLAlchemy
	db = SQLAlchemy()
	context.setup_user_roles()

@manager.command
def create_initial_db():
	from migrations import Migrations
	Migrations.create_initial_db()

@manager.command
def db_migrate():
    from migrations import Migrations
    Migrations.db_migrate()

@manager.command
def db_upgrade():
    from migrations import Migrations
    Migrations.db_upgrade()

@manager.command
def db_downgrade():
    from migrations import Migrations
    Migrations.db_downgrade()



if __name__ == '__main__':
	manager.run()
