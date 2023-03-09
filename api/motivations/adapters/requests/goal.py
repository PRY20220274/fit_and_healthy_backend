from api.motivations.adapters.docs.goal import goal_namespace
from flask_restx import fields


goal_request = goal_namespace.model('GoalRequest', {
    'description': fields.String(required=True)
})
