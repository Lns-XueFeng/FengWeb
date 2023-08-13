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

    def login(self, username=None, password=None):
        if username is None and password is None:
            username = "XueFeng"
            password = "123456789"
        res = self.client.post(
            url_for("auth.login"),
            data={"username": "XueFeng", "password": "123456789"},
            follow_redirects=True
        )
        return res

    def logout(self):
        return self.client.get(url_for("auth.logout"), follow_redirects=True)
