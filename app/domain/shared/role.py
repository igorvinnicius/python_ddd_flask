class Role(object):
	def __init__(self, id=None, name=None, description=None, users=[]):
		self.id = id
		self.name = name
		self.description = description
		self.users=users


class Role_Name:
	ADMIN = 'ADMIN'
	USER = 'USER'
	BLOGER = 'BLOGER'
