from flask import Blueprint
from flask_restx import Api
from api.motivations.controllers.frequency import frequency_namespace
from api.motivations.controllers.activity import activity_namespace
from api.motivations.controllers.objective import objective_namespace
from api.motivations.controllers.food_goal import food_goal_namespace
from api.motivations.controllers.physical_goal import physical_goal_namespace
from api.motivations.controllers.goal import goal_namespace

motivations_blueprint = Blueprint('motivations_api', __name__, url_prefix='/motivations-api')
api = Api(motivations_blueprint, title='Motivations API', description='Motivations api', doc='/doc')

api.add_namespace(frequency_namespace)
api.add_namespace(activity_namespace)
api.add_namespace(objective_namespace)
api.add_namespace(food_goal_namespace)
api.add_namespace(physical_goal_namespace)
api.add_namespace(goal_namespace)
