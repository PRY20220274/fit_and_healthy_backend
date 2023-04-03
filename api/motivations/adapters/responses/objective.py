from api.motivations.adapters.docs.objective import objective_namespace
from flask_restx import fields


objective_response = objective_namespace.model('ObjectiveResponse', {
    'id': fields.Integer,
    'name': fields.String
})
