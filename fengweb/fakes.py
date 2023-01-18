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
    name_list = ["Python", "Spider", "DataAnlysis", "Algorithm", "Auto", "Blogweb"]
    title_list = ["为什么选择Python？", "用爬虫窥探这个世界！", "数据分析真的很难吗？",
                  "准备好感受算法之美！", "享受自动化的便利吧！", "快来一起搭建网站吧！"]
    about_list = ["人生苦短，我学Python！Python是人人都能学会的编程语言，本笔记包含Python简介，Python基础，Python进阶以及常用的库！",
                  "在入门Python之后怎能不赶快写出让人为之振奋的脚本呢？简单几行代码就能爬取海量数据，没错，这就是爬虫！",
                  "在这个大数据且信息爆炸的时代，怎能不挖掘信息为我用之？从海量信息中分析出有价值的信息同样是不可多得的一种能力！",
                  "Python是我们的武器和招式，但数据结构和算法却是我们的内力，武器在好招式在多也比不过内力雄厚的至强之人！",
                  "你有被日常工作中重复且枯燥的琐事缠身吗？Python能让你逃离单调无味重复的工作，让你充分利用自己的时间去做想做的事！",
                  "从零开始开发一个网站就好像看着自己的孩子长大一样，他可能功能不多，页面简单，但他是你一点一滴的结晶..."]
    for name, title, about in zip(name_list, title_list, about_list):
        notes = Notes(
            name=name,
            title=title,
            about=about
        )
        db.session.add(notes)
    db.session.commit()
