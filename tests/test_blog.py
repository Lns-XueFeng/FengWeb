from fengweb.extensions import db
from fengweb.models import Notes

from tests.base import BaseTest


class BlogTest(BaseTest):
    
    def setUp(self):
        super(BlogTest, self).setUp()

        notes = Notes(name="test", title="test", about="this is a test")

        db.session.add_all([notes])
        db.session.commit()

    def test_index(self):
        client = self.client.get("/")
        data = client.text
        self.assertIn("回到古代见李白", data)
        self.assertIn("test", data)
