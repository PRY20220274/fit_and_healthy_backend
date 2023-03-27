from flask import request
from flask_restx import Resource
from domain.commons.util import get_param
from api.recommendations.adapters.docs.food_recommendation import food_namespace
from api.recommendations.adapters.responses.food_recommendation import food_response
from domain.recommendations.schemas.food_recommendation import FoodRecommendationSchema
from domain.recommendations.services.food_recommendation import get_recommendations_by_user, get_today_recommendation
from domain.commons.util import get_user

@food_namespace.route('')
class FoodRecommendationListResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.schema = FoodRecommendationSchema(many=True)

    @food_namespace.marshal_list_with(food_response, code=200, description='Success')
    @food_namespace.response(code=400, description='Bad Request')
    def get(self):
        user = get_user()
        recommendations = get_recommendations_by_user(user)
        response = self.schema.dump(recommendations)
        return response, 200


@food_namespace.route('/today')
class FoodRecommendationTodayResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.schema = FoodRecommendationSchema()

    @food_namespace.response(code=201, description='Success', model=food_response)
    @food_namespace.response(code=400, description='Bad Request')
    def get(self):
        user = get_user()
        recommendation = get_today_recommendation(user)
        response = self.schema.dump(recommendation)
        return response, 200
