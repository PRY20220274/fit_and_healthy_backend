from flask import Blueprint
from flask_restx import Api
from api.recommendations.controllers.food_recommendation import food_namespace
from api.recommendations.controllers.physical_recommendation import physical_namespace

recommendations_blueprint = Blueprint('recommendations_api', __name__, url_prefix='/recommendations-api')
api = Api(recommendations_blueprint, title='Recommendations API', description='Recommendations api', doc='/doc')

api.add_namespace(food_namespace)
api.add_namespace(physical_namespace)
