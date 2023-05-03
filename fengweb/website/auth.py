from flask import Blueprint
from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_required, logout_user, login_user

from fengweb.forms import LoginForm
from fengweb.models import Admin
from fengweb.utils import redirect_back


auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("blog.index"))

    login_form = LoginForm()
    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data
        remember = login_form.remember.data
        admin = Admin.query.first()
        if admin:
            if username == admin.username and admin.validate_password(password):
                login_user(admin, remember)
                flash("登陆成功！")
                return redirect_back()
            else:
                flash("登录失败！")
        else:
            flash("用户不存在！")
    return render_template("auth/login.html", login_form=login_form)


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("你已退出登录！")
    return redirect_back()
