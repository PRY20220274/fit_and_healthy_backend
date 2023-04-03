from api.motivations.adapters.docs.food_goal import food_goal_namespace
from api.accounts.adapters.responses.user import user_response
from flask_restx import fields


food_goal_response = food_goal_namespace.model('FoodGoalResponse', {
    'id': fields.Integer,
    'description': fields.String,
    'activity': fields.String,
    'objective': fields.String,
    'completed': fields.String
})
