from flask import Blueprint
from flask_restx import Api
from api.questionnaires.controllers.questionnaire_category import category_namespace
from api.questionnaires.controllers.questionnaire import questionnaire_namespace

questionnaires_blueprint = Blueprint('questionnaires_api', __name__, url_prefix='/questionnaires-api')
api = Api(questionnaires_blueprint, title='Questionnaires API', description='Questionnaires api', doc='/doc')

api.add_namespace(category_namespace)
api.add_namespace(questionnaire_namespace)
