from api.motivations.adapters.docs.physical_goal import physical_goal_namespace
from flask_restx import fields


physical_goal_response = physical_goal_namespace.model('PhysicalGoalResponse', {
    'id': fields.Integer,
    'description': fields.String,
    'steps': fields.Integer,
    'kilometers': fields.Integer,
    'calories': fields.Integer,
    'cardio_points': fields.Integer,
    'frequency': fields.String,
    'completed': fields.String
})
