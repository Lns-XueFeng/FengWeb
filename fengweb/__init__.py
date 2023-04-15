import os
import click
import random

from flask import Flask, render_template
from flask_wtf.csrf import CSRFError

from .models import Admin, Category, Link, Post
from .extensions import bootstrap4, db, login_manager, ckeditor, moment, csrf
from .apis import api_bp
from .blueprints.blog import blog_bp
from .blueprints.admin import admin_bp
from .blueprints.auth import auth_bp
from .settings import config


base_dir = os.path.abspath(os.path.dirname(__file__))


def make_app(config_name=None):
    if config_name is None:
        config_name = os.getenv("FLASK_ENV", "development")

    app = Flask("fengweb")
    app.config.from_object(config[config_name])

    app.register_blueprint(blog_bp)
    app.register_blueprint(admin_bp, url_prefix="/admin")
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(api_bp, url_prefix="/data/api/v1.0")

    bootstrap4.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    ckeditor.init_app(app)
    moment.init_app(app)
    csrf.init_app(app)

    register_commands(app)
    register_template_context(app)
    register_errors(app)
    register_shell_context(app)

    return app


def register_commands(app):
    @app.cli.command()
    @click.option("--drop", is_flag=True, help="Create after drop")
    def initdb(drop):
        """初始化数据库"""
        if drop:
            click.confirm("此操作将会删除数据库, 是否继续？", abort=True)
            db.drop_all()
            click.echo("已删除")
        db.create_all()
        click.echo("初始化数据库")

    @app.cli.command()
    @click.option("--category", default=10, help="分类的数量, 默认为10")
    @click.option("--post", default=50, help="文章的数量, 默认为50")
    def forge(category, post):
        """生成一些假数据进行填充"""
        from fengweb.fakes import fake_categories, fake_posts, fake_links, set_notes, fake_message
        db.drop_all()
        db.create_all()

        click.echo(f"生成ing {category} categories...")
        fake_categories(category)

        click.echo(f"生成ing {post} posts...")
        fake_posts(post)

        click.echo("生成ing links...}")
        fake_links()

        click.echo("生成ing name title about for notes...")
        set_notes()

        click.echo("生成ing messages...")
        fake_message()

        click.echo("生成完成")

    @app.cli.command()
    @click.option("--username", prompt=True, help="用户登录名称")
    @click.option("--password", prompt=True, confirmation_prompt=True, help="用户登录密码")
    def init_admin(username, password):
        """建立管理员账户以及默认分类"""
        click.echo("正在初始化数据库...")
        db.create_all()

        admin = Admin.query.first()
        if admin is not None:
            click.echo("此管理员已存在, 更新ing...")
            admin.username = username
            admin.set_password(password)
        else:
            click.echo("创建管理员账户...")
            admin = Admin(username=username)
            admin.set_password(password)
            db.session.add(admin)

        category = Category.query.first()
        if category is None:
            click.echo("创建默认分类...")
            category = Category(name="Default")
            db.session.add(category)

        db.seesion.commit()
        click.echo("创建完成")


def register_template_context(app):
    @app.context_processor
    def make_template_context():
        path = base_dir + "\\static\\musics"
        all_files = os.listdir(path)
        rand_music = random.choice(all_files).split(".")[0]
        admin = Admin.query.first()
        categories = Category.query.order_by(Category.name).all()
        links = Link.query.order_by(Link.name).all()
        return dict(rand_music=rand_music, admin=admin, categories=categories, links=links)


def register_errors(app):
    @app.errorhandler(400)
    def bad_request(e):
        return render_template("error/400.html"), 400

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("errors/404.html"), 404

    @app.errorhandler(500)
    def internal_server_error():
        return render_template("errors/500"), 500

    @app.errorhandler(CSRFError)
    def handle_csrf_error(e):
        return render_template("error/400.html", description=e.description), 400


def register_shell_context(app):
    @app.shell_context_processor
    def make_shell_context():
        return dict(db=db, Admin=Admin, Post=Post, Category=Category)
