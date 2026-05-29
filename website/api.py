from flask import Blueprint, jsonify, request
from .models import Note
from . import db

api = Blueprint('api', __name__)


@api.route('/notes', methods=['GET'])
def get_notes():


    notes = Note.query.all()

    result = []

    for note in notes:
        result.append({
            "id": note.id,
            "data": note.data,
             "user_id": note.user_id
        })

    return jsonify(result), 200


@api.route('/notes', methods=['POST'])
def create_note():

    data = request.get_json()

    if not data or not data.get("data"):
            return jsonify({
                "error": "Note data is required"
            }), 400

    new_note = Note(
        data=data["data"],
        user_id=1
    )

    db.session.add(new_note)
    db.session.commit()

    return jsonify({
        "message": "Note created successfully",
        "id": new_note.id,
        "data": new_note.data
    }), 201


@api.route('/notes/<int:id>', methods=['GET'])
def get_note(id):

    note = Note.query.get(id)

    if not note:
        return jsonify({
            "error": "Note not found"
        }), 404

    return jsonify({
        "id": note.id,
        "data": note.data,
        "user_id": note.user_id
    }), 200

@api.route('/notes/<int:id>', methods=['PUT'])
def update_note(id):

    note = Note.query.get(id)

    if not note:
        return jsonify({
            "error": "Note not found"
        }), 404

    data = request.get_json()

    if not data.get("data"):
        return jsonify({
            "error": "Note data is required"
        }), 400

    note.data = data["data"]

    db.session.commit()

    return jsonify({
        "message": "Note updated successfully",
        "id": note.id,
        "data": note.data
    }), 200