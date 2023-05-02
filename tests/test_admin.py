from fengweb.extensions import db

from tests.base import BaseTest


class TestAdmin(BaseTest):

    def setUp(self):
        super(TestAdmin, self).setUp()
        self.login()

    def test_upload_md(self):
        pass
