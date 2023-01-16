from flask import Blueprint
from flask import render_template


blog_bp = Blueprint("blog", __name__)


@blog_bp.route("/")
def index():
    return render_template("blog/index.html")


@blog_bp.route("/passages")
def passages():
    return render_template("blog/passages.html")


@blog_bp.route("/messages")
def messages():
    return render_template("blog/message_wall.html")


@blog_bp.route("/music")
def music():
    return render_template("blog/music.html")


@blog_bp.route("/about")
def about():
    return render_template("blog/about.html")


@blog_bp.route("/detail_notes/int:post_id>")
def detail_notes(post_id):
    return render_template("blog/detail_notes.html")


@blog_bp.route("/detail_passage/int:post_id>")
def detail_passage(post_id):
    return render_template("blog/detail_passage.html")
