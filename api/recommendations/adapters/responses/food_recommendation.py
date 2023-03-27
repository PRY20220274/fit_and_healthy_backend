from api.recommendations.adapters.docs.food_recommendation import food_namespace
from flask_restx import fields

food_response = food_namespace.model('FoodResponse', {
    'id': fields.Integer,
    'description': fields.String
})
