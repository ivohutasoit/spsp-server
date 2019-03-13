from flask import abort, Blueprint, request, jsonify
from geopy.geocoders import Nominatim

region_controller = Blueprint('region_controller', __name__)

@region_controller.route('/geocode', methods=['POST'])
def geocode():
    latitude = longitude = None
    if request.json:
        if not 'latitude' in request.json or not 'longitude' in request.json:
            abort(400)
        else:
            latitude = request.json['latitude']
            longitude = request.json['longitude']
    elif request.form:
        if not 'latitude' in request.form or not 'longitude' in request.form:
            abort(400)
        else:
            latitude = request.form['latitude']
            longitude = request.form['longitude']
    
    error = None

    if not latitude:
        error = 'latitude is required'
    elif not longitude:
        error = 'longitude is required'

    if not error:
        geolocator = Nominatim(user_agent="Softhaxi Browser")
        location = geolocator.reverse(latitude + ", " + longitude)
        """ raw = location.raw
        data = {
            'country_code': str.upper(raw['address']['country_code']),
            'state': raw['address']['state'],
            'postcode': raw['address']['postcode']
        } """
        return jsonify({ 'status': 'OK', 'data': location.raw }), 200
    else: return jsonify({ 'status': 'ERROR', 'error': error }), 400