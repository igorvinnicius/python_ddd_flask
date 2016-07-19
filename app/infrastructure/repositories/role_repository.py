from app.domain.shared.role import Role
import repository_base

class RoleRepository(repository_base.RepositoryBase):

    def __init__(self):
        super(RoleRepository, self).__init__()
