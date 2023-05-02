from fengweb.extensions import db

from tests.base import BaseTest


class TestAuth(BaseTest):
     def setUp(self):
         super(TestAuth, self).setUp()

     def test_login(self):
         pass

     def test_logout(self):
         self.login()
         pass
