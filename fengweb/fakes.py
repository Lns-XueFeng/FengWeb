import random

from faker import Faker
from sqlalchemy.exc import IntegrityError

from fengweb.extensions import db
from fengweb.models import Post, Category, Link, Notes, Message


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


def fake_message():
    for _ in range(50):
        message = Message(
            name=fake.name(),
            about=fake.sentence(),
        )
        db.session.add(message)
    db.session.commit()


def set_notes():
    name_list = ["Rust", "Python", "Algorithm", "Spider", "Flask", "SQL(MySQL)"]
    about_list = ["Rust是一门强调安全、性能和并发性的系统编程语言，它在速度媲美C++的同时又防止了开发者对内存的误操作行为！",
                  "Python是人人都能学会的编程语言，本笔记包含Python简介，Python基础，Python进阶以及常用的库！",
                  "编程语言只是我们的武器和招式，但数据结构和算法却是我们的内力，武器再好招式再多也比不过内力雄厚的至强之人！",
                  "通过写爬虫你可以爬取海量的数据，文章、图片、音乐甚至是视频，所见即所得！",
                  "Flask是一个灵巧的微框架，给予了开发者最大的发挥空间，为快速开发应用提供了极大的便利！",
                  "熟练编写SQL操作数据库非常重要，在编程中总是会用到，本笔记将会包含SQL语句、MySQL的记录！"]
    for name, about in zip(name_list, about_list):
        notes = Notes(
            name=name,
            title=name,
            about=about
        )
        db.session.add(notes)
    db.session.commit()
