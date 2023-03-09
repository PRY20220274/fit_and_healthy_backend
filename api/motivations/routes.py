from flask import Blueprint
from flask_restx import Api
from api.motivations.controllers.frequency import frequency_namespace
from api.motivations.controllers.motivation_type import motivation_type_namespace
from api.motivations.controllers.phrase import phrase_namespace
from api.motivations.controllers.goal import goal_namespace

motivations_blueprint = Blueprint('motivations_api', __name__, url_prefix='/motivations-api')
api = Api(motivations_blueprint, title='Motivations API', description='Motivations api', doc='/doc')

api.add_namespace(frequency_namespace)
api.add_namespace(motivation_type_namespace)
api.add_namespace(phrase_namespace)
api.add_namespace(goal_namespace)
