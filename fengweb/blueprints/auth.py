from flask import Blueprint
from flask import render_template, flash
from flask_login import current_user

from fengweb.forms import LoginForm
from fengweb.models import Admin


auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        pass

    login_form = LoginForm()
    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data
        admin = Admin.query.first()
        if admin:
            if username == admin.username and admin.validate_password(password):
                flash("登陆成功！")
                return render_template("admin/admin.html")
            else:
                flash("登录失败！")
        else:
            flash("用户不存在！")
    return render_template("auth/login.html", login_form=login_form)
