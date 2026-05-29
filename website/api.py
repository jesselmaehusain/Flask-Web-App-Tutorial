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