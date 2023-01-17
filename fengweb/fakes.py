import random

from faker import Faker
from sqlalchemy.exc import IntegrityError

from fengweb.extensions import db
from fengweb.models import Post, Category, Link


fake = Faker("zh_CN")


def fake_posts(count=50):
    for _ in range(count):
        post = Post(
            title=fake.sentence(),
            body=fake.text(2000),
            category=Category.query.get(random.randint(1, Category.query.count())),
            timestamp=fake.date_time_this_year()
        )

        db.session.add(post)
    db.session.commit()


def fake_categories(count=10):
    category = Category(name="Default")
    db.session.add(category)

    for _ in range(count):
        category = Category(name=fake.word())
        db.session.add(category)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()


def fake_links():
    twitter = Link(name="Twitter", url="#")
    facebook = Link(name="Facebook", url="#")
    linkedin = Link(name="LinkedIn", url="#")
    google = Link(name="Google+", url="#")
    db.session.add_all([twitter, facebook, linkedin, google])
    db.session.commit()
