import unittest

from flask import url_for

from fengweb import make_app
from fengweb.extensions import db
from fengweb.models import Admin


class BaseTest(unittest.TestCase):

    def setUp(self):
        app = make_app("test")
        self.context = app.test_request_context()
        self.context.push()
        self.client = app.test_client()
        self.runner = app.test_cli_runner()

        db.create_all()
        user = Admin(username="XueFeng")
        user.set_password("123456789")
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        db.drop_all()
        self.context.pop()
