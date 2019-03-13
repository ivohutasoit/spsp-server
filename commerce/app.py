from flask import Flask, jsonify, make_response
from controllers import category_controller, tender_controller

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index(): 
    return 'Welcome to Pasang commerce service'

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

app.register_blueprint(category_controller, url_prefix='/api/v1.0/commerce/categories')
app.register_blueprint(tender_controller, url_prefix='/api/v1.0/commerce/tender')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)