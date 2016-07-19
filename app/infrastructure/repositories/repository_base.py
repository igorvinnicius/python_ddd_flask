from flask.ext.sqlalchemy import SQLAlchemy



class RepositoryBase(object):
	def __init__(self):
		self.db = SQLAlchemy()

	def session(self):
		return self.db.session

	def create(self, entity):
		self.session().add(entity)
		self.session().commit()

	def save(self, entity):
		self.session().add(entity)
		self.session().commit()
