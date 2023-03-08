from api.motivations.adapters.docs.frequency import frequency_namespace
from flask_restx import fields


frequency_response = frequency_namespace.model('FrequencyResponse', {
    'id': fields.Integer,
    'name': fields.String
})
