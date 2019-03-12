from flask import abort, Blueprint, jsonify, request

category_controller = Blueprint('category_controller', __name__)

categories = [
    {
        'id': 1,
        'name': u'Culture Fashion',
        #'description': u'Pasang Tender for requesting some goods, services, contracts etc'
    },
    {
        'id': 2,
        'name': u'Modern Fashion',
        #'description': u'Pasang Tender for requesting some goods, services, contracts etc'
    },
    {
        'id': 3,
        'name': u'Household',
        #'description': u'Pasang Tender for requesting some goods, services, contracts etc'
    },
    {
        'id': 4,
        'name': u'Office & Stasionery',
        #'description': u'Pasang Tender for requesting some goods, services, contracts etc'
    },
    {
        'id': 5,
        'name': u'Event',
        #'description': u'Pasang Tender for requesting some goods, services, contracts etc'
    },
    {
        'id': 6,
        'name': u'Otomotive',
        #'description': u'Pasang Tender for requesting some goods, services, contracts etc'
    },
    {
        'id': 7,
        'name': u'Customer Goods',
        #'description': u'Pasang Tender for requesting some goods, services, contracts etc'
    }
]

@category_controller.route('', methods=['GET'])
def list():
    return jsonify({ 'status': 'OK', 'data': categories }), 200

@category_controller.route('/<int:id>', methods=['GET'])
def detail(id):
    category = [category for category in categories if category['id'] == id]
    if len(category) == 0:
        abort(404)
    return jsonify({ 'status': 'OK', 'category': category[0] }), 200

@category_controller.route('', methods=['POST'])
def create():
    title = None
    if request.json:
        if not 'title' in request.json:
            abort(400)
        else:
            title = request.json['title']
    elif request.form:
        if not 'title' in request.form:
            abort(400)
        else:
            title = request.form['title']
    else: abort(400)

    error = None
    if not title:
        error = 'Title is required'
    
    if error is None:
        category = {
            'id': categories[-1]['id'] + 1,
            'title': title
        }
        categories.append(category)

        return jsonify({ 'status': 'OK', 'category': category }), 201
    else: return jsonify({ 'status': 'ERROR', 'error': error }), 201

@category_controller.route('/<int:id>', methods=['PUT'])
def update(id):
    category = [category for category in categories if category['id']==id]
    if len(category) == 0:
        abort(400)
    title = None

    if request.json:
        if not 'title' in request.json:
            abort(400)
        elif type(request.json['title']) != str:
            abort(400)
        else:
            title = request.json['title']
    elif request.form:
        if not 'title' in request.form:
            abort(400)
        elif type(request.form['title']) != str:
            abort(400)
        else:
            title = request.form['title']

    error = None

    if not title:
        error = 'Title is required'
    
    category[0]['title'] = title

    if error is None:
        return jsonify({ 'status': 'OK', 'category': category[0] }), 200
    else: return jsonify({ 'status': 'ERROR', 'error': error }), 200

@category_controller.route('/<int:id>', methods=['DELETE'])
def delete(id):
    category = [category for category in categories if category['id']==id]
    if len(category) == 0:
        abort(400)
    categories.remove(category[0])
    return jsonify({ 'status': 'OK', 'category': category[0], 'result': True }), 200