from api.motivations.adapters.docs.motivation_type import motivation_type_namespace
from flask_restx import fields


motivation_type_response = motivation_type_namespace.model('MotivationTypeResponse', {
    'id': fields.Integer,
    'name': fields.String
})
