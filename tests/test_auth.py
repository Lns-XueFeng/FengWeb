from flask import url_for, current_app

from fengweb.models import Admin
from fengweb.extensions import db

from tests.base import BaseTest


class TestAuth(BaseTest):
    def setUp(self):
        super(TestAuth, self).setUp()

    def test_login(self):
        client = self.client.get("auth.login")
        data = client.text
        self.assertIn("Login", data)

        client = self.client.post(
            url_for("auth.login"),
            data={"username": "XueFeng", "password": "123456789"},
            follow_redirects=True
        )
        data = client.text
        self.assertIn("登陆成功！", data)

    def test_login_fail(self):
        client = self.client.post(
            url_for("auth.login"),
            data={"username": "XueFeng", "password": "---------"},
            follow_redirects=True
        )
        data = client.text
        self.assertIn("Login", data)

    def test_login_no_user(self):
        db.session.delete(Admin.query.filter_by(username="XueFeng").first())
        client = self.client.post(
            url_for("auth.login"),
            data={"username": "XueFeng", "password": "123456789"},
            follow_redirects=True
        )
        data = client.text
        self.assertIn("Login", data)

    def test_logout(self):
        self.login()
        res = self.logout()
        data = res.text
        self.assertIn("你已退出登录！", data)
