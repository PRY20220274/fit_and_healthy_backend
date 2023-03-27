from flask import request
from flask_restx import Resource
from domain.commons.util import get_param
from api.recommendations.adapters.docs.physical_recommendation import physical_namespace
from api.recommendations.adapters.responses.physical_recommendation import physical_response
from domain.recommendations.schemas.physical_recommendation import PhysicalRecommendationSchema
from domain.recommendations.services.physical_recommendation import get_recommendations_by_user, get_today_recommendation
from domain.commons.util import get_user

@physical_namespace.route('')
class PhysicalRecommendationListResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.schema = PhysicalRecommendationSchema(many=True)

    @physical_namespace.marshal_list_with(physical_response, code=200, description='Success')
    @physical_namespace.response(code=400, description='Bad Request')
    def get(self):
        user = get_user()
        recommendations = get_recommendations_by_user(user)
        response = self.schema.dump(recommendations)
        return response, 200


@physical_namespace.route('/today')
class PhysicalRecommendationTodayResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.schema = PhysicalRecommendationSchema()

    @physical_namespace.response(code=201, description='Success', model=physical_response)
    @physical_namespace.response(code=400, description='Bad Request')
    def get(self):
        user = get_user()
        recommendation = get_today_recommendation(user)
        response = self.schema.dump(recommendation)
        return response, 200
