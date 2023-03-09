from api.motivations.adapters.docs.goal import goal_namespace
from api.accounts.adapters.responses.user import user_response
from flask_restx import fields


goal_response = goal_namespace.model('GoalResponse', {
    'id': fields.Integer,
    'description': fields.String,
    'frequency': fields.String,
    'type': fields.String,
    'user': fields.Nested(user_response)
})
