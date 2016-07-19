class Company(object):
	def __init__(self,id=None,
					name=None,
					email=None,
                    domain=None,
					users=[]
				):

		self.id = id
		self.name = name
		self.email = email	
        self.domain = domain
		self.users=users
