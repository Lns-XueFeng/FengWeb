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
    name_list = ["C", "Python", "Backend", "Algorithm", "Database", "Network"]
    about_list = ["C语言古老而强大，简单而灵活，是其他语言的基石，比如Python的底层就是C进行的实现！",
                  "Python是人人都能学会的编程语言，本笔记包含Python简介，Python基础，Python进阶以及常用的库！",
                  "Backend中将包含爬虫、前端三剑客、Flask框架以及个人网站项目，其中大多在Github中，这里只放置其链接！",
                  "编程语言只是我们的武器和招式，但数据结构和算法却是我们的内力，武器再好招式再多也比不过内力雄厚的至强之人！",
                  "熟练编写SQL操作数据库非常重要，在编程中总是会用到，本笔记将会包含SQL语句、MySQL的记录！",
                  "当你在浏览器中输入一个网址到浏览器返回给你漂亮的页面，短短几秒的过程，究竟经过了怎样的过程才到达了我们的身边？"]
    for name, about in zip(name_list, about_list):
        notes = Notes(
            name=name,
            title=name,
            about=about
        )
        db.session.add(notes)
    db.session.commit()
