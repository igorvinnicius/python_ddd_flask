class Survey(object):
	def __init__(self,id=None,
					name=None,
                    description=None,
					creator=None,
                    creation_date=None,
                    total_points=None,
                    private=None,
                    visible=None,
                    active=None,
					questions=[]
				):

		self.id = id
		self.name = name
		self.description = description
		self.creator = creator
		self.creation_date = creation_date
		self.total_points = total_points
		self.private = private
		self.visible
		self.active
		self.questions=questions
