from flask import jsonify

from . import api_bp
from ..models import Link


@api_bp.route("/query/links", methods=["GET"])
def get_link():
    links = Link.query.all()
    if links:
        data = {}
        for lo in links:
            data[lo.name] = lo.url
        return jsonify(data)
    return jsonify({"links": None})


@api_bp.route("/query/links/<int:link_id>", methods=["GET"])
def get_a_link(link_id):
    link = Link.query.get(link_id)
    if link:
        return jsonify({link.name: link.url})
    return jsonify({f"link_{link_id}": None})


# post, delete, put