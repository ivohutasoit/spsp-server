from flask import Blueprint, jsonify

tender_controller = Blueprint('tender_controller', __name__)

tenders = [
    {
        'id': 1,
        'title': u'House for team building',
        'content': u'We need a house for team building around Pematangsiantar. ' +
                    'This event will be established from 2 April 2019 until 10 April. ' + 
                    'Member number is 200 persons. Please contact to WhatsApp +6283423566328',
        'validity': {
            'from': u'12 March 2019',
            'to': u'1 April 2019'
        },
        'thumbnail': {
            'small': u'https://picsum.photos/240/100?image=120',
            'medium': u'https://picsum.photos/320/180?image=120',
            'large': u'https://picsum.photos/360/240?image=120'
        },
        'like': 0,
        'comment': 0,
        'share': 0,
        'location': {
            'latitude': 0.0,
            'longitude': 0.0,
            'geolocation': u''
        }
    }, {
        'id': 2,
        'title': u'Ulos Batak 500 pieces',
        'content': u'Urgently needed!!! For wedding at 19 March 2019 at Balige',
        'validity': {
            'from': u'12 March 2019',
            'to': u'16 March 2019'
        },
        'thumbnail': {
            'small': u'https://picsum.photos/240/100?image=121',
            'medium': u'https://picsum.photos/320/180?image=121',
            'large': u'https://picsum.photos/360/240?image=121'
        },
        'like': 0,
        'comment': 0,
        'share': 0,
        'location': {
            'latitude': 0.0,
            'longitude': 0.0,
            'geolocation': u''
        }
    }
]

@tender_controller.route('', methods=['GET'])
def tenderList():
    return jsonify({ 'status': 'OK', 'data': tenders }), 200