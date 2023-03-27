from api.recommendations.adapters.docs.physical_recommendation import physical_namespace
from flask_restx import fields

physical_response = physical_namespace.model('PhysicalResponse', {
    'id': fields.Integer,
    'description': fields.String
})
