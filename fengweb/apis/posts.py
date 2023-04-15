from flask import jsonify

from . import api_bp
from ..models import Post, Category


@api_bp.route("/query/categories", methods=["GET"])
def get_categories():
    categories = Category.query.all()
    if categories:
        data = {}
        for co in categories:
            data[f"category_{co.id}"] = {"name": co.name}
        return jsonify(data)
    return jsonify({"categories": None})


@api_bp.route("/query/categories/<int:category_id>", methods=["GET"])
def get_a_category(category_id):
    category = Category.query.get(category_id)
    if category:
        return jsonify({f"category_{category.id}": category.name})
    return jsonify({f"category_{category_id}": None})


@api_bp.route("/query/posts", methods=["GET"])
def get_posts():
    posts = Post.query.all()
    if posts:
        data = {}
        for po in posts:
            data[f"post_{po.id}"] = {"title": po.title, "body": po.body}
        return jsonify(data)
    return jsonify({"posts": None})


@api_bp.route("/query/posts/<int:post_id>", methods=["GET"])
def get_a_post(post_id):
    post = Post.query.get(post_id)
    if post:
        return jsonify({f"post_{post.id}": {"title": post.title, "body": post.body}})
    return jsonify({f"post_{post_id}": None})


# post, delete, put
