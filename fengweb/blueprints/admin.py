import os

from flask import Blueprint
from flask import render_template, flash, redirect, session, url_for, request, current_app
from flask_login import login_required

from fengweb.extensions import db
from fengweb.forms import UploadMarkdown, PassageSubmit, PassageEdit, MessageEdit
from fengweb.models import Post, Message, Category
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
    per_page = current_app.config["BLUELOG_MANAGE_MESSAGE_PER_PAGE"]
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(page=page, per_page=per_page)
    posts = pagination.items
    return render_template("admin/manage_passage.html", page=page, pagination=pagination, posts=posts)


@admin_bp.route("/new_passage", methods=["GET", "POST"])
@login_required
def new_passage():
    form = PassageEdit()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        category = Category.query.get(form.category.data)
        post = Post(title=title, body=body)
        category.posts.append(post)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for("admin.manage_passage"))
    return render_template("admin/new_passage.html", form=form)


@admin_bp.route("/edit_passage/<int:post_id>", methods=["GET", "POST"])
@login_required
def edit_passage(post_id):
    form = PassageSubmit()
    post = Post.query.get(post_id)
    if form.validate_on_submit():
        title = form.title.data
        category = Category.query.get(form.category.data)
        body = form.body.data
        post = Post(title=title, body=body)
        category.posts.append(post)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for("admin.manage_passage"))
    form.title.data = post.title
    form.category.data = post.category_id
    form.body.data = post.body
    return render_template("admin/edit_passage.html", form=form)


@admin_bp.route("/delete_passage/<int:post_id>", methods=["GET", "POST"])
@login_required
def delete_passage(post_id):
    post = Post.query.get(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect_back()


@admin_bp.route("/manage_message")
@login_required
def manage_message():
    page = request.args.get("page", 1, type=int)
    per_page = current_app.config["BLUELOG_MANAGE_POST_PER_PAGE"]
    pagination = Message.query.order_by(Message.timestamp.desc()).paginate(page=page, per_page=per_page)
    message_list = pagination.items
    return render_template("admin/manage_message.html", page=page, pagination=pagination, messages=message_list)


@admin_bp.route("/edit_message/<int:message_id>", methods=["GET", "POST"])
@login_required
def edit_message(message_id):
    form = MessageEdit()
    message = Message.query.get(message_id)
    if form.validate_on_submit():
        name = form.name.data
        about = form.about.data
        message = Message(name=name, about=about)
        db.session.add(message)
        db.session.commit()
        return redirect(url_for("admin.manage_message"))
    form.name.data = message.name
    form.about.data = message.about
    return render_template("admin/edit_message.html", form=form)


@admin_bp.route("/delete_message/<int:message_id>", methods=["GET", "POST"])
@login_required
def delete_message(message_id):
    message = Message.query.get(message_id)
    db.session.delete(message)
    db.session.commit()
    return redirect_back()


@admin_bp.route("/manage_category")
@login_required
def manage_category():
    return render_template("admin/manage_category.html")
