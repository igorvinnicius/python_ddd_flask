from enum import Enum

class Answer(object):
	def __init__(self,id=None,
					description=None,
					creator=None,
                    creation_date=None,
					question=None,
                    answer_type=None
				):

		self.id = id
		self.description = description
		self.creator = creator
		self.creation_date = creation_date
		self.question = question
		self.answer_type = answer_type

class AnswerType(Enum):
    unique = 1,
    multiple = 2
