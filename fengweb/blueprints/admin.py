import os

from flask import Blueprint
from flask import render_template, flash, redirect, session, url_for, request, current_app
from flask_login import login_required

from fengweb.forms import UploadMarkdown
from fengweb.models import Post, Message
from fengweb.utils import redirect_back


admin_bp = Blueprint("admin", __name__)


@admin_bp.route("/upload_md", methods=["GET", "POST"])
@login_required
def upload_md():
    form = UploadMarkdown()
    if form.validate_on_submit():
        f = form.file.data
        file_name = f.filename
        f.save(os.path.join(current_app.config["UPLOAD_MARKDOWN_PATH"], file_name))
        flash(f"上传{file_name}成功")
        session["filenames"] = [file_name]
        return redirect(url_for("blog.index"))
    return render_template("admin/upload_md.html", form=form)


@admin_bp.route("/manage_passage")
@login_required
def manage_passage():
    page = request.args.get("page", 1, type=int)
    per_page = current_app.config["BLUELOG_MANAGE_POST_PER_PAGE"]
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(page=page, per_page=per_page)
    posts = pagination.items
    return render_template("admin/manage_passage.html", page=page, pagination=pagination, posts=posts)


@admin_bp.route("/new_passage")
@login_required
def new_passage():
    return render_template("admin/new_passage.html")


@admin_bp.route("/edit_passage/<int:post_id>")
@login_required
def edit_passage():
    return render_template("admin/edit_passage.html")


@admin_bp.route("/edit_passage/<int:post_id>")
@login_required
def delete_passage():
    return redirect_back()


@admin_bp.route("/manage_message")
@login_required
def manage_message():
    page = request.args.get("page", 1, type=int)
    per_page = current_app.config["BLUELOG_MANAGE_POST_PER_PAGE"]
    pagination = Message.query.order_by(Message.timestamp.desc()).paginate(page=page, per_page=per_page)
    message_list = pagination.items
    return render_template("admin/manage_message.html", page=page, pagination=pagination, messages=message_list)


@admin_bp.route("/edit_message/<int:message_id>")
@login_required
def edit_message():
    pass


@admin_bp.route("/edit_message/<int:message_id>")
@login_required
def delete_message():
    pass


@admin_bp.route("/manage_category")
@login_required
def manage_category():
    return render_template("admin/manage_category.html")
