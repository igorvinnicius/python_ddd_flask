import unittest
from app.domain.services.authentication_service import AuthenticationService

class AuthenticationServiceTest(unittest.TestCase):

    def test_generate_hash(self):
        hash = AuthenticationService.generate_hash('password')
        self.assertTrue(hash is not None)

    def test_check_password_true(self):
        hash = AuthenticationService.generate_hash('password')
        password_true = AuthenticationService.check_password(hash, 'password')
        self.assertTrue(password_true)

    def test_check_password_false(self):
        hash = AuthenticationService.generate_hash('password')
        password_false = AuthenticationService.check_password(hash, 'password_false')
        self.assertFalse(password_false)
