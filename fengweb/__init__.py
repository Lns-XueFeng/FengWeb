import os
import click
import random

from flask import Flask, g

from .extensions import bootstrap4, db, login_manager, ckeditor, moment
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

    bootstrap4.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    ckeditor.init_app(app)
    moment.init_app(app)

    register_commands(app)
    register_global(app)

    return app


def register_commands(app):
    @app.cli.command()
    @click.option('--drop', is_flag=True, help='Create after drop.')
    def initdb(drop):
        if drop:
            click.confirm('This operation will delete the database, do you want to continue?', abort=True)
            db.drop_all()
            click.echo('Drop tables.')
        db.create_all()
        click.echo('Initialized database.')

    @app.cli.command()
    @click.option('--category', default=10, help='Quantity of categories, default is 10.')
    @click.option('--post', default=50, help='Quantity of posts, default is 50.')
    def forge(category, post):
        """Generate fake data."""
        from fengweb.fakes import fake_categories, fake_posts, fake_links, set_notes, fake_message

        db.drop_all()
        db.create_all()

        click.echo('Generating %d categories...' % category)
        fake_categories(category)

        click.echo('Generating %d posts...' % post)
        fake_posts(post)

        click.echo('Generating links...')
        fake_links()

        click.echo("Generating name title about for notes...")
        set_notes()

        click.echo("Generating messages...")
        fake_message()

        click.echo('Done.')


def register_global(app):
    @app.context_processor
    def get_rand_music():
        path = base_dir + "\\static\\musics"
        all_files = os.listdir(path)
        rand_music = random.choice(all_files).split(".")[0]
        return {"rand_music": rand_music}

