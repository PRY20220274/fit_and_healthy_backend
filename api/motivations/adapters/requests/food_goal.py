from api.motivations.adapters.docs.food_goal import food_goal_namespace
from flask_restx import fields


food_goal_request = food_goal_namespace.model('FoodGoalRequest', {
    'activity': fields.Integer(required=True),
    'objective': fields.Integer(required=True)
})
