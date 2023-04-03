from api.motivations.adapters.docs.goal import goal_namespace
from flask_restx import fields


goal_response = goal_namespace.model('GoalResponse', {
    'message': fields.String,
})
