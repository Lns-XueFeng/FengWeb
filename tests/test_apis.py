from flask import url_for

from fengweb.extensions import db
from fengweb.models import Link, Message, Notes, Post, Category
from tests.base import BaseTest


class TestApis(BaseTest):

    def setUp(self):
        super(TestApis, self).setUp()
        link = Link(name="Lns-XueFeng", url="https://www.github.com/Lns-XueFeng")
        message = Message(name="test", about="this is a test")
        note = Notes(name="test", title="test", about="this is a test")
        category = Category(name="Default")
        post = Post(title="test", body="this is a test", category=category)

        db.session.add_all([link, message, note, category, post])
        db.session.commit()

    def test_get_link(self):
        client = self.client.get(url_for("apis.get_link"))
        data = client.text
        self.assertIn("Lns-XueFeng", data)

    def test_not_get_link(self):
        link = Link.query.get(1)
        db.session.delete(link)
        db.session.commit()
        client = self.client.get(url_for("apis.get_link"))
        data = client.json
        self.assertIn("error", data)

    def test_get_a_link(self):
        client = self.client.get(url_for("apis.get_a_link", link_id=1))
        data = client.text
        self.assertIn("Lns-XueFeng", data)

    def test_not_get_a_link(self):
        link = Link.query.get(1)
        db.session.delete(link)
        db.session.commit()
        client = self.client.get(url_for("apis.get_a_link", link_id=1))
        data = client.json
        self.assertIn("error", data)

    def test_get_messages(self):
        client = self.client.get(url_for("apis.get_messages"))
        data = client.text
        self.assertIn("test", data)

    def test_not_get_messages(self):
        message = Message.query.get(1)
        db.session.delete(message)
        db.session.commit()
        client = self.client.get(url_for("apis.get_messages"))
        data = client.json
        self.assertIn("error", data)

    def test_get_a_message(self):
        client = self.client.get(url_for("apis.get_a_message", message_id=1))
        data = client.text
        self.assertIn("test", data)

    def test_not_get_a_message(self):
        message = Message.query.get(1)
        db.session.delete(message)
        db.session.commit()
        client = self.client.get(url_for("apis.get_a_message", message_id=1))
        data = client.json
        self.assertIn("error", data)

    def test_get_notes(self):
        client = self.client.get(url_for("apis.get_notes"))
        data = client.text
        self.assertIn("test", data)

    def test_not_get_notes(self):
        note = Notes.query.get(1)
        db.session.delete(note)
        db.session.commit()
        client = self.client.get(url_for("apis.get_notes"))
        data = client.json
        self.assertIn("error", data)

    def test_get_a_note(self):
        client = self.client.get(url_for("apis.get_a_note", note_id=1))
        data = client.text
        self.assertIn("test", data)

    def test_not_get_a_note(self):
        note = Notes.query.get(1)
        db.session.delete(note)
        db.session.commit()
        client = self.client.get(url_for("apis.get_a_note", note_id=1))
        data = client.json
        self.assertIn("error", data)

    def test_get_categories(self):
        client = self.client.get(url_for("apis.get_categories"))
        data = client.text
        self.assertIn("Default", data)

    def test_not_get_categories(self):
        category = Category.query.get(1)
        db.session.delete(category)
        db.session.commit()
        client = self.client.get(url_for("apis.get_categories"))
        data = client.json
        self.assertIn("error", data)

    def test_get_a_category(self):
        client = self.client.get(url_for("apis.get_a_category", category_id=1))
        data = client.text
        self.assertIn("Default", data)

    def test_not_get_a_category(self):
        category = Category.query.get(1)
        db.session.delete(category)
        db.session.commit()
        client = self.client.get(url_for("apis.get_a_category", category_id=1))
        data = client.json
        self.assertIn("error", data)

    def test_get_posts(self):
        client = self.client.get(url_for("apis.get_posts"))
        data = client.text
        self.assertIn("test", data)

    def test_not_get_posts(self):
        post = Post.query.get(1)
        db.session.delete(post)
        db.session.commit()
        client = self.client.get(url_for("apis.get_posts"))
        data = client.text
        self.assertIn("error", data)

    def test_get_a_post(self):
        client = self.client.get(url_for("apis.get_a_post", post_id=1))
        data = client.text
        self.assertIn("test", data)

    def test_not_get_a_post(self):
        post = Post.query.get(1)
        db.session.delete(post)
        db.session.commit()
        client = self.client.get(url_for("apis.get_a_post", post_id=1))
        data = client.json
        self.assertIn("error", data)
