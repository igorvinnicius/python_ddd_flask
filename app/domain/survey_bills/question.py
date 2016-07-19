class Question(object):
	def __init__(self,id=None,
					description=None,
					creator=None,
                    creation_date=None,
                    value_points=None,
                    survey=None,
					answers=[]
				):

		self.id = id
		self.description = description
		self.creator = creator
		self.creation_date = creation_date
		self.value_points = value_points
		self.survey = survey
		self.answers=answers
