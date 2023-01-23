import os

from flask import Blueprint
from flask import render_template, request, current_app

from fengweb.utils import md_to_html, redirect_back
from fengweb.models import Post, Notes, Message
from fengweb.forms import LeftWords
from fengweb.extensions import db


blog_bp = Blueprint("blog", __name__)

base_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


@blog_bp.route("/")
def index():
    notes = Notes.query.all()
    return render_template("blog/index.html", notes=notes)


@blog_bp.route("/passages")
def passages():
    page = request.args.get("page", 1, type=int)
    per_page = current_app.config["BLUELOG_POST_PER_PAGE"]
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(page=page, per_page=per_page)
    posts = pagination.items
    return render_template("blog/passages.html", pagination=pagination, posts=posts)


@blog_bp.route("/messages")
def messages():
    page = request.args.get("page", 1, type=int)
    per_page = current_app.config["BLUELOG_POST_PER_PAGE"]
    pagination = Message.query.order_by(Message.timestamp.desc()).paginate(page=page, per_page=per_page)
    message_list = pagination.items
    return render_template("blog/message_wall.html", pagination=pagination, message_list=message_list)


@blog_bp.route("/music")
def music():
    count = 0
    path = base_dir + "\\static\\musics"
    all_files = os.listdir(path)
    music_list = []
    for file in all_files:
        count = count + 1
        song_name = file.split(".")[0]
        music_list.append((str(count), song_name))
    return render_template("blog/music.html", music_list=music_list)


@blog_bp.route("/about")
def about():
    return render_template("blog/about.html")


@blog_bp.route("/detail_passage/<int:post_id>")
def detail_passage(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("blog/detail_passage.html", post=post)


@blog_bp.route("/category_passage/<int:category_id>")
def category_passage(category_id):
    pass


@blog_bp.route("/show_notes/<name>")
def show_notes(name):
    html_string = md_to_html("fengweb/static/markdown/{}.md".format(name))
    return render_template("blog/show_markdown.html", content=html_string)


@blog_bp.route("/left_words", methods=["GET", "POST"])
def left_words():
    form = LeftWords()
    if form.validate_on_submit():
        name = form.name.data
        words = form.words.data
        message = Message(name=name, about=words)
        db.session.add(message)
        db.session.commit()
        return redirect_back()
    return render_template("blog/left_words.html", form=form)
