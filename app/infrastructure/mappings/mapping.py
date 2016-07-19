from sqlalchemy import ForeignKey, PrimaryKeyConstraint, Integer, String, Boolean, Text, DateTime, Enum
from sqlalchemy.orm import mapper, relationship
from sqlalchemy.orm import column_property
from sqlalchemy import select, func, and_

from flask.ext.sqlalchemy import SQLAlchemy

from app.domain.shared.user import User
from app.domain.shared.role_user import Role_User
from app.domain.shared.role import Role
from app.domain.survey_bills.answer import Answer, AnswerType
from app.domain.survey_bills.survey import Survey
from app.domain.survey_bills.question import Question



from sqlalchemy import Table, MetaData, Column

metadata = MetaData()

def init(db):

	# Shared Domain ------------------------------------------------------------------

	# User Mapping
	user_mapping = db.Table('user', metadata,
		db.Column('id', Integer, primary_key=True),
		db.Column('name', String(50)),
		db.Column('email', String(100)),
		db.Column('password_hash',String(200)),
		db.Column('confirmed', Boolean)
	)

	#Role_User Mapping
	role_user_mapping = db.Table('role_user', metadata,
		db.Column('role_id', Integer, ForeignKey('role.id')),
		db.Column('user_id', Integer, ForeignKey('user.id')),
		db.PrimaryKeyConstraint('role_id', 'user_id', name='role_user_pk')
	)

	#Role Mapping
	role_mapping = db.Table('role', metadata,
		db.Column('id', Integer, primary_key=True),
		db.Column('name', String(50)),
		db.Column('description', String(200)),
	)

	# Survey Bills Domain ------------------------------------------------------------------

	#Survey Mapping
	survey_mapping = db.Table('survey', metadata,
		db.Column('id', Integer, primary_key=True),
		db.Column('name', String(200)),
		db.Column('description', String(2000)),
		db.Column('creator', Integer, ForeignKey('user.id')),
		db.Column('creation_date', DateTime),
		db.Column('total_points', Integer),
		db.Column('private', Boolean),
		db.Column('visible', Boolean),
		db.Column('active', Boolean)
	)

	#Question Mapping
	question_mapping = db.Table('question', metadata,
		db.Column('id', Integer, primary_key=True),
		db.Column('name', String(200)),
		db.Column('description', String(2000)),
		db.Column('creator', Integer, ForeignKey('user.id')),
		db.Column('creation_date', DateTime),
		db.Column('value_points', Integer),
		db.Column('survey', Integer, ForeignKey('survey.id')),

	)

	#Answer Mapping
	answer_mapping = db.Table('answer', metadata,
		db.Column('id', Integer, primary_key=True),
		db.Column('name', String(200)),
		db.Column('description', String(2000)),
		db.Column('creator', Integer, ForeignKey('user.id')),
		db.Column('creation_date', DateTime),
		db.Column('value_points', Integer),
		db.Column('question', Integer, ForeignKey('question.id')),
		db.Column('answer_type', Integer)

	)

	# Mappers ------------------------------------------------------------------

	# Shared Domain Mappers------------------------------------------------------------------

	#User Mapper
	db.mapper(User, user_mapping, properties={

		'is_admin': column_property(
						select([func.count(role_user_mapping.c.user_id) > 0],
						and_(
							role_user_mapping.c.user_id==user_mapping.c.id,
							role_user_mapping.c.role_id==role_mapping.c.id and role_mapping.name == 'ADMIN'
						))),

		'is_bloger': column_property(
						select([func.count(role_user_mapping.c.user_id) > 0],
						and_(
							role_user_mapping.c.user_id==user_mapping.c.id,
							role_user_mapping.c.role_id==role_mapping.c.id and role_mapping.name == 'BLOGER'
						))),

		'roles' : relationship(Role, secondary=role_user_mapping),
		# 'surveys' : relationship(Survey, backref='user', lazy='dynamic', primaryjoin="User.id==Survey.creator"),
		# 'questions' : relationship(Question, backref='user', lazy='dynamic', primaryjoin="User.id==Question.creator"),
		# 'answers' : relationship(Answer, backref='user', lazy='dynamic', primaryjoin="User.id==Answer.creator")
	})

	# Role_User Mapper
	db.mapper(Role_User, role_user_mapping)

	#Role Mapper
	db.mapper(Role, role_mapping, properties={

		'users' : relationship(User, secondary=role_user_mapping)

	})

	# Survey Bills Domain Mappers------------------------------------------------------------------

	#Survey Mapper
	db.mapper(Survey, survey_mapping, properties={

		'questions' : relationship(Question, lazy='dynamic')

	})

	#Question Mapper
	db.mapper(Question, question_mapping, properties={

		'answers' : relationship(Answer, lazy='dynamic')

	})

	#Answer Mapper
	db.mapper(Answer, answer_mapping)
