from flask import jsonify, Blueprint

error_bp = Blueprint('error', __name__)

@error_bp.errorhandler(400)
def handle_bad_request(error):
    response = {
        'error': 'Bad Request'
    }
    return jsonify(response), 400

@error_bp.errorhandler(401)
def handle_unauthorized(error):
    response = {
        'error': 'Unauthorized'
    }
    return jsonify(response), 401

@error_bp.errorhandler(404)
def handle_not_found(error):
    response = {
        'error': 'Not Found'
    }
    return jsonify(response), 404

@error_bp.errorhandler(500)
def handle_internal_server_error(error):
    response = {
        'error': 'Internal Server Error'
    }
    return jsonify(response), 500