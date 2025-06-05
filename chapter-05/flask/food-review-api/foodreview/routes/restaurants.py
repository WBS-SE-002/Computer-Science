from flask import Blueprint, request, jsonify
from ..db import get_connection
from ..utils.auth_utils import require_auth

restaurants_bp = Blueprint('restaurants', __name__, url_prefix='/restaurants')


@restaurants_bp.post('/')
@require_auth
def create():
    return jsonify({'message': 'Restaurant created'})
