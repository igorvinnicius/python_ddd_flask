from flask.ext.login import UserMixin, AnonymousUserMixin


class User(object):
	def __init__(self,id=None,
					name=None,
					email=None,
					password=None,
					password_hash=None,
					confirmed=None,
					roles=[],
					surveys=[],
					questions=[],
					answers=[]
				):

		self.id = id
		self.name = name
		self.email = email
		self.password = password
		self.password_hash = password_hash
		self.confirmed = confirmed
		self.roles=roles
		self.surveys = surveys
		self.questions = questions
		self.answers = answers



	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return self.id
