from app.domain.shared.user import User
import repository_base

class UserRepository(repository_base.RepositoryBase):

    def __init__(self):
        super(UserRepository, self).__init__()

    def get_by_id(self, id):
        try:
            return self.session().query(User).filter_by(id=id).one()
        except:
            return None

    def get_by_name(self, name):
        try:
            return self.session().query(User).filter_by(name=name).one()
        except:
            return None

    def get_by_email(self, email):
        try:
            return self.session().query(User).filter_by(email=email).one()
        except:
            return None
