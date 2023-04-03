from api.motivations.adapters.docs.activity import activity_namespace
from flask_restx import fields


activity_response = activity_namespace.model('ActivityResponse', {
    'id': fields.Integer,
    'name': fields.String
})
