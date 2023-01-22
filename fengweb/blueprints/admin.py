from flask import Blueprint
from flask import render_template

from flask_login import login_required


admin_bp = Blueprint("admin" ,__name__)


@admin_bp.route("/upload_md")
@login_required
def upload_md():
    return render_template("admin/upload_md.html")


@admin_bp.route("/new_passage")
@login_required
def new_passage():
    return render_template("admin/new_passage.html")


@admin_bp.route("/edit_passage")
@login_required
def edit_passage():
    return render_template("admin/edit_passage.html")


@admin_bp.route("/manage_passage")
@login_required
def manage_passage():
    return render_template("admin/manage_passage.html")


@admin_bp.route("/manage_message")
@login_required
def manage_message():
    return render_template("admin/manage_message.html")


@admin_bp.route("/manage_category")
@login_required
def manage_category():
    return render_template("admin/manage_category.html")
