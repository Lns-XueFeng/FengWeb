import os

from flask import Flask

from .extensions import bootstrap4, db, login_manager, ckeditor
from .blueprints.blog import blog_bp
from .blueprints.admin import admin_bp
from .blueprints.auth import auth_bp
from .settings import config


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

    return app
