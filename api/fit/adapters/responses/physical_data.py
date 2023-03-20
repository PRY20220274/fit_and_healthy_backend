from api.fit.adapters.docs.physical_data import physical_data_namespace
from flask_restx import fields


physical_data_response = physical_data_namespace.model('PhysicalDataResponse', {
    'id': fields.Integer,
    'steps': fields.Integer,
    'calories': fields.Integer,
    'cardio_points': fields.Integer,
    'heart_rate': fields.Integer,
    'breathing_rate': fields.Integer,
    'kilometers_traveled': fields.Integer,
    'created_at': fields.String
})
