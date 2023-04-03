from api.motivations.adapters.docs.physical_goal import physical_goal_namespace
from flask_restx import fields


physical_goal_request = physical_goal_namespace.model('PhysicalGoalRequest', {
    'steps': fields.Integer(required=True),
    'kilometers': fields.Integer(required=True),
    'calories': fields.Integer(required=True),
    'cardio_points': fields.Integer(required=True),
    'frequency': fields.Integer(required=True)
})
