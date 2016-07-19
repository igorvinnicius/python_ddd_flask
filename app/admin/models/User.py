class User:
	def __init__(self,id=None, name=None, email=None, password=None, password_hash=None, posts=[])
		self.id = id
		self.name = name
		self.email = email
		self.password = password
		self.password_hash = password_hash
		self.posts = posts
