import os
import sys


basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

WIN = sys.platform.startswith("win")
if WIN:
    prefix = "sqlite:///"
else:
    prefix = "sqlite:////"


class BaseConfig(object):
    SECRET_KEY = os.getenv("SECRET_KEY", "dev key")

    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    CKEDITOR_ENABLE_CSRF = True

    FENGWEB_POST_PER_PAGE = 6
    FENGWEB_MANAGE_POST_PER_PAGE = 15
    FENGWEB_MANAGE_MESSAGE_PER_PAGE = 15
    FENGWEB_SLOW_QUERY_THRESHOLD = 1
    UPLOAD_MARKDOWN_PATH = basedir + "/fengweb/static/markdown/"


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = prefix + os.path.join(basedir, 'data-dev.db')


class TestingConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", prefix + os.path.join(basedir, "data.db"))


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "test": TestingConfig,
}
