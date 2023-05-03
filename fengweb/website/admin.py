import os

from flask import Blueprint
from flask import render_template, flash, redirect, session, url_for, request, current_app
from flask_login import login_required

from fengweb.extensions import db
from fengweb.forms import UploadMarkdown, PassageSubmit, PassageEdit, MessageEdit, CategorySubmit, CategoryEdit
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
        flash(f"上传{file_name}成功！")
        session["filenames"] = [file_name]
        return redirect(url_for("blog.index"))
    return render_template("admin/upload_md.html", form=form)


@admin_bp.route("/manage_passage")
@login_required
def manage_passage():
    page = request.args.get("page", 1, type=int)
    per_page = current_app.config["FENGWEB_MANAGE_MESSAGE_PER_PAGE"]
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(page=page, per_page=per_page)
    posts = pagination.items
    return render_template("admin/manage_passage.html", page=page, pagination=pagination, posts=posts)


@admin_bp.route("/manage_passage/new_passage", methods=["GET", "POST"])
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
        flash("新文章已创建！")
        return redirect(url_for("admin.manage_passage"))
    return render_template("admin/new_passage.html", form=form)


@admin_bp.route("/manage_passage/edit_passage/<int:post_id>", methods=["GET", "POST"])
@login_required
def edit_passage(post_id):
    form = PassageSubmit()
    post = Post.query.get(post_id)
    if form.validate_on_submit():
        post.title = form.title.data
        post.category = Category.query.get(form.category.data)
        post.body = form.body.data
        db.session.commit()
        flash("文章已更新！")
        return redirect(url_for("admin.manage_passage"))
    form.title.data = post.title
    form.category.data = post.category_id
    form.body.data = post.body
    return render_template("admin/edit_passage.html", form=form)


@admin_bp.route("/manage_passage/delete_passage/<int:post_id>", methods=["GET", "POST"])
@login_required
def delete_passage(post_id):
    post = Post.query.get(post_id)
    db.session.delete(post)
    db.session.commit()
    flash("文章删除成功！")
    return render_template("admin/manage_passage.html")


@admin_bp.route("/manage_message")
@login_required
def manage_message():
    page = request.args.get("page", 1, type=int)
    per_page = current_app.config["FENGWEB_MANAGE_POST_PER_PAGE"]
    pagination = Message.query.order_by(Message.timestamp.desc()).paginate(page=page, per_page=per_page)
    message_list = pagination.items
    return render_template("admin/manage_message.html", page=page, pagination=pagination, messages=message_list)


@admin_bp.route("/manage_message/edit_message/<int:message_id>", methods=["GET", "POST"])
@login_required
def edit_message(message_id):
    form = MessageEdit()
    message = Message.query.get(message_id)
    if form.validate_on_submit():
        message.name = form.name.data
        message.about = form.about.data
        db.session.commit()
        flash("留言已更新！")
        return redirect(url_for("admin.manage_message"))
    form.name.data = message.name
    form.about.data = message.about
    return render_template("admin/edit_message.html", form=form)


@admin_bp.route("/manage_message/delete_message/<int:message_id>", methods=["GET", "POST"])
@login_required
def delete_message(message_id):
    message = Message.query.get(message_id)
    db.session.delete(message)
    db.session.commit()
    flash("留言删除成功！")
    return render_template("admin/manage_message.html")


@admin_bp.route("/manage_category")
@login_required
def manage_category():
    category_list = Category.query.all()
    return render_template("admin/manage_category.html", category_list=category_list)


@admin_bp.route("/manage_category/new_category", methods=["GET", "POST"])
@login_required
def new_category():
    form = CategorySubmit()
    if form.validate_on_submit():
        name = form.name.data
        n_category = Category(name=name)
        db.session.add(n_category)
        db.session.commit()
        flash("新分类已创建！")
        return redirect_back()
    return render_template("admin/new_category.html", form=form)


@admin_bp.route("/manage_category/edit_category/<int:category_id>", methods=["GET", "POST"])
@login_required
def edit_category(category_id):
    form = CategoryEdit()
    category = Category.query.get(category_id)
    if form.validate_on_submit():
        category.name = form.name.data
        db.session.commit()
        flash("分类已更新！")
        return redirect(url_for("admin.manage_category"))
    form.name.data = category.name
    return render_template("admin/edit_category.html", form=form)


@admin_bp.route("/delete_category/<int:category_id>", methods=["GET", "POST"])
@login_required
def delete_category(category_id):
    category = Category.query.get(category_id)
    if category.id == 1:
        flash("你不能删除默认分类！")
        return redirect_back()
    category.delete()
    flash("分类已删除！")
    return render_template("admin/manage_category.html")
