from flask import Blueprint
from flask import render_template, request, current_app

from fengweb.utils import md_to_html
from fengweb.models import Post


blog_bp = Blueprint("blog", __name__)


@blog_bp.route("/")
def index():
    return render_template("blog/index.html")


@blog_bp.route("/passages")
def passages():
    page = request.args.get("page", 1, type=int)
    per_page = current_app.config["BLUELOG_POST_PER_PAGE"]
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(page=page, per_page=per_page)
    posts = pagination.items
    return render_template("blog/passages.html", pagination=pagination, posts=posts)


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


@blog_bp.route("/show_notes/<name>")
def show_notes(name):
    html_string = md_to_html("fengweb/static/markdown/{}.md".format(name))
    return render_template("blog/show_markdown.html", content=html_string)
