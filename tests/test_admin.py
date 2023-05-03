from flask import url_for

from fengweb.extensions import db
from fengweb.models import Post, Category, Message
from tests.base import BaseTest


class TestAdmin(BaseTest):

    def setUp(self):
        super(TestAdmin, self).setUp()
        self.login()
        category = Category(name="Default")
        post = Post(title="test", body="this is a test", category=category)
        message = Message(name="test", about="this is a test")

        db.session.add_all([category, post, message])
        db.session.commit()

    def test_upload_md(self):
        pass

    def test_manage_passages(self):
        client = self.client.get(url_for("admin.manage_passage"))
        data = client.text
        self.assertIn("test", data)

    def test_new_passage(self):
        db.session.delete(Post.query.get(1))
        client = self.client.post(url_for(
            "admin.new_passage",
            data={"title": "test", "body": "this is a test"},
            follow_redirects=True))
        data = client.text
        self.assertIn("test", data)

    def test_edit_passage(self):
        client = self.client.post(url_for(
            "admin.edit_passage", post_id=1,
            data={"title": "new_test", "body": "this is a test"},
            follow_redirects=True))
        data = client.text
        self.assertIn("new_test", data)

    def test_show_edit_passage(self):
        client = self.client.get(url_for(
            "admin.edit_passage", post_id=1, follow_redirects=True))
        data = client.text
        self.assertIn("test", data)

    def test_delete_passage(self):
        client = self.client.get(url_for(
            "admin.delete_passage", post_id=1, follow_redirects=True))
        data = client.text
        self.assertNotIn("test", data)
        self.assertIn("No Passages.", data)

    def test_manage_message(self):
        client = self.client.get(url_for("admin.manage_message"))
        data = client.text
        self.assertIn("test", data)

    def test_edit_message(self):
        client = self.client.post(url_for(
            "admin.edit_message", message_id=1,
            data={"name": "new_test", "about": "this is a test"},
            follow_redirects=True))
        data = client.text
        self.assertIn("new_test", data)

    def test_show_edit_message(self):
        client = self.client.get(url_for(
            "admin.edit_message", message_id=1, follow_redirects=True))
        data = client.text
        self.assertIn("test", data)

    def test_delete_message(self):
        client = self.client.get(url_for(
            "admin.delete_message", message_id=1, follow_redirects=True))
        data = client.text
        self.assertNotIn("test", data)
        self.assertIn("No Messages.", data)

    def test_manage_category(self):
        client = self.client.get(url_for("admin.manage_category"))
        data = client.text
        self.assertIn("Default", data)

    def test_new_category(self):
        client = self.client.post(url_for(
            "admin.new_category",
            data={"name": "new_test"},
            follow_redirects=True))
        data = client.text
        self.assertIn("new_test", data)

    def test_edit_category(self):
        client = self.client.post(url_for(
            "admin.edit_category",
            category_id=1,
            data={"name": "edit_test"},
            follow_redirects=True))
        data = client.text
        self.assertIn("edit_test", data)

    def test_show_edit_category(self):
        client = self.client.get(url_for(
            "admin.edit_category", category_id=1))
        data = client.text
        self.assertIn("Default", data)

    def test_delete_category(self):
        client = self.client.get(url_for(
            "admin.delete_category", category_id=1))
        data = client.text
        self.assertNotIn("Default", data)
        self.assertIn("No Category.", data)
