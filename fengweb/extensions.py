from flask_bootstrap import Bootstrap4
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_ckeditor import CKEditor
from flask_moment import Moment
from flask_wtf import CSRFProtect


bootstrap4 = Bootstrap4()
db = SQLAlchemy()
login_manager = LoginManager()
ckeditor = CKEditor()
moment = Moment()
csrf = CSRFProtect()


@login_manager.user_loader
def load_user(user_id):
    from fengweb.models import Admin
    user = Admin.query.get(int(user_id))
    return user


login_manager.login_view = 'auth.login'
# login_manager.login_message = 'Your custom message'
login_manager.login_message_category = 'warning'
