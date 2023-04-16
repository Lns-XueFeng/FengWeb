from flask import jsonify, redirect

from . import api_bp
from ..models import Notes


@api_bp.route("/query/notes", methods=["GET"])
def get_notes():
    notes = Notes.query.all()
    if notes:
        data = {}
        for no in notes:
            data[f"note_{no.id}"] = {"title": no.title, "about": no.about}
        return jsonify(data)
    return redirect("not_found")


@api_bp.route("/query/notes/<int:note_id>", methods=["GET"])
def get_a_note(note_id):
    note = Notes.query.get(note_id)
    if note:
        return jsonify({f"note_{note.id}": {"title": note.title, "about": note.about}})
    return redirect("not_found")


# post, delete, put
