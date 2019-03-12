from flask import Blueprint, jsonify

category_controller = Blueprint('category_controller', __name__)

@category_controller.route('/', methods=['GET', 'POST'])
def list():
    return jsonify({ 'status': 'OK', 'data':[] }), 200