from flask import jsonify, redirect

from . import api_bp
from ..models import Message


@api_bp.route("/query/messages", methods=["GET"])
def get_messages():
    messages = Message.query.all()
    if messages:
        data = {}
        for mo in messages:
            data[f"message_{mo.id}"] = {"name": mo.name, "about": mo.about, "time": mo.timestamp}
        return jsonify(data)
    return redirect("not_found")


@api_bp.route("/query/messages/<int:message_id>", methods=["GET"])
def get_a_message(message_id):
    message = Message.query.get(message_id)
    if message:
        return jsonify(
            {f"message_{message_id}": {"name": message.name, "about": message.about, "time": message.timestamp}}
        )
    return redirect("not_found")


# post, delete, put
