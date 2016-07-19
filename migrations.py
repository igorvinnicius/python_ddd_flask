import os
from migrate.versioning import api
from flask.ext.sqlalchemy import SQLAlchemy

class Migrations:

    @staticmethod
    def create_initial_db():
        from config import config
        from app.infrastructure.mappings import mapping
        from app.infrastructure.mappings.mapping import metadata
        db = SQLAlchemy()
        config = config[os.getenv('FLASK_CONFIG') or 'default']
        metadata.create_all(db.engine)

        if not os.path.exists(config.SQLALCHEMY_MIGRATE_REPO):
            api.create(config.SQLALCHEMY_MIGRATE_REPO, 'database repository')
            api.version_control(config.SQLALCHEMY_DATABASE_URI, config.SQLALCHEMY_MIGRATE_REPO)
        else:
            api.version_control(config.SQLALCHEMY_DATABASE_URI, config.SQLALCHEMY_MIGRATE_REPO, api.version(config.SQLALCHEMY_MIGRATE_REPO))


    @staticmethod
    def db_migrate():
        import imp
        from config import config
        from app.infrastructure.mappings import mapping
        from app.infrastructure.mappings.mapping import metadata
        db = SQLAlchemy()
        config = config[os.getenv('FLASK_CONFIG') or 'default']
        metadata.create_all(db.engine)
        v = api.db_version(config.SQLALCHEMY_DATABASE_URI, config.SQLALCHEMY_MIGRATE_REPO)
        migration = config.SQLALCHEMY_MIGRATE_REPO + ('/versions/%03d_migration.py' % (v+1))
        tmp_module = imp.new_module('old_model')
        old_model = api.create_model(config.SQLALCHEMY_DATABASE_URI, config.SQLALCHEMY_MIGRATE_REPO)
        exec(old_model, tmp_module.__dict__)
        script = api.make_update_script_for_model(config.SQLALCHEMY_DATABASE_URI, config.SQLALCHEMY_MIGRATE_REPO, tmp_module.meta, metadata)
        open(migration, "wt").write(script)
        api.upgrade(config.SQLALCHEMY_DATABASE_URI, config.SQLALCHEMY_MIGRATE_REPO)
        v = api.db_version(config.SQLALCHEMY_DATABASE_URI, config.SQLALCHEMY_MIGRATE_REPO)
        print('New migration saved as ' + migration)
        print('Current database version: ' + str(v))

    @staticmethod
    def db_upgrade():
        from config import config
        config = config[os.getenv('FLASK_CONFIG') or 'default']
        api.upgrade(config.SQLALCHEMY_DATABASE_URI, config.SQLALCHEMY_MIGRATE_REPO)
        v = api.db_version(config.SQLALCHEMY_DATABASE_URI, config.SQLALCHEMY_MIGRATE_REPO)
        print('Current database version: ' + str(v))

    @staticmethod
    def db_downgrade():
        from config import config
        config = config[os.getenv('FLASK_CONFIG') or 'default']
        v = api.db_version(config.SQLALCHEMY_DATABASE_URI, config.SQLALCHEMY_MIGRATE_REPO)
        api.downgrade(config.SQLALCHEMY_DATABASE_URI, config.SQLALCHEMY_MIGRATE_REPO, v - 1)
        v = api.db_version(config.SQLALCHEMY_DATABASE_URI, config.SQLALCHEMY_MIGRATE_REPO)
        print('Current database version: ' + str(v))
