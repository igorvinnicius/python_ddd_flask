class Context:
    def __init__(self, db):
        from flask.ext.sqlalchemy import SQLAlchemy
        from app.infrastructure.mappings import mapping
        from app.infrastructure.repositories import user_repository

        self.db = db

        mapping.init(db)

        self.user_repository = user_repository.UserRepository()


    def setup(self, db):
        from app.infrastructure.mappings import mapping
        from app.infrastructure.mappings.mapping import metadata
        mapping.init(db)
        print db.engine
        # metadata.create_all(current_app.config.get('SQLALCHEMY_DATABASE_URI))
        metadata.create_all(db.engine)

    def setup_user_roles(self):

        from app.domain.shared.role import Role_Name, Role
        from app.infrastructure.repositories.role_repository import RoleRepository

        role_repository = RoleRepository()

        roles =  [
            Role(name=Role_Name.ADMIN, description='Full access'),
            Role(name=Role_Name.USER, description='Read Only access'),
            Role(name=Role_Name.BLOGER, description='Blog access')
        ]

        for r in roles:
            role_repository.create(r)


    def create_initial_db(self):
        from config import config
        from app.infrastructure.mappings import mapping
        from app.infrastructure.mappings.mapping import metadata

        # user_mapping.init(self.db)
        config = config[os.getenv('FLASK_CONFIG') or 'default']
        metadata.create_all(self.db.engine)
        # db.create_all()

        if not os.path.exists(config.SQLALCHEMY_MIGRATE_REPO):
            api.create(config.SQLALCHEMY_MIGRATE_REPO, 'database repository')
            api.version_control(config.SQLALCHEMY_DATABASE_URI, config.SQLALCHEMY_MIGRATE_REPO)
        else:
            api.version_control(config.SQLALCHEMY_DATABASE_URI, config.SQLALCHEMY_MIGRATE_REPO, api.version(config.SQLALCHEMY_MIGRATE_REPO))
