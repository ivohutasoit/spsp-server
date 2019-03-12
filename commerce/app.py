from flask import Flask
from .controllers import category_controller

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index(): 
    return 'Welcome to Pasang commerce service'

app.register_blueprint(category_controller, url_prefix='/api/v1.0/commerce/categories')

if __name__ == '__main__':
    app.run(debug=True, port='5000')