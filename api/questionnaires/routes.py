from flask import Blueprint
from flask_restx import Api

questionnaires_blueprint = Blueprint('questionnaires_api', __name__, url_prefix='/questionnaires-api')
api = Api(questionnaires_blueprint, title='Questionnaires API', description='Questionnaires api', doc='/doc')
