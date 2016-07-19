from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
role = Table('role', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=50)),
    Column('description', VARCHAR(length=200)),
)

role_user = Table('role_user', pre_meta,
    Column('role_id', INTEGER, primary_key=True, nullable=False),
    Column('user_id', INTEGER, primary_key=True, nullable=False),
)

user = Table('user', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=50)),
    Column('email', VARCHAR(length=100)),
    Column('password_hash', VARCHAR(length=200)),
    Column('confirmed', BOOLEAN),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['role'].drop()
    pre_meta.tables['role_user'].drop()
    pre_meta.tables['user'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['role'].create()
    pre_meta.tables['role_user'].create()
    pre_meta.tables['user'].create()
