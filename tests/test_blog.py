from flask import url_for

from fengweb.extensions import db
from fengweb.models import Notes, Post, Category, Message
from tests.base import BaseTest


class BlogTest(BaseTest):
    
    def setUp(self):
        super(BlogTest, self).setUp()

        notes = Notes(name="test", title="test", about="this is a test")
        category = Category(name="Default")
        post = Post(title="test", body="this is a test", category=category)
        message = Message(name="test", about="this is a test")

        db.session.add_all([notes, category, post, message])
        db.session.commit()

    def test_index(self):
        client = self.client.get(url_for("blog.index"))
        data = client.text
        self.assertIn("回到古代见李白", data)
        self.assertIn("播放", data)
        self.assertIn("test", data)

    def test_passages(self):
        client = self.client.get(url_for("blog.passages"))
        data = client.text
        self.assertIn("test", data)

    def test_messages(self):
        client = self.client.get(url_for("blog.messages"))
        data = client.text
        self.assertIn("test", data)

    def test_music(self):
        client = self.client.get(url_for("blog.music"))
        data = client.text
        self.assertIn("一路向北", data)

    def test_about(self):
        client = self.client.get(url_for("blog.about"))
        data = client.text
        self.assertIn("其实，人生在世，是不太需要其他人的建议的！", data)

    def test_detail_passage(self):
        client = self.client.get(url_for("blog.detail_passage", post_id=1))
        data = client.text
        self.assertIn("this is a test", data)

    def test_show_notes(self):
        client = self.client.get(url_for("blog.show_notes", name="Python"))
        data = client.text
        self.assertIn("本文档为Lns-XueFeng原创笔记", data)

    def test_left_words(self):
        client = self.client.get(url_for("blog.left_words"))
        data = client.text
        self.assertIn("留下你想说的话", data)

        client = self.client.post(
            url_for("blog.left_words"),
            data={"name": "test", "about": "this is a test"}
        )
        data = client.text
        self.assertIn("test", data)

    def test_category_passages(self):
        client = self.client.get(url_for("blog.category_passage", category_id=1))
        data = client.text
        self.assertIn("test", data)
