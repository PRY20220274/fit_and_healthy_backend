from flask import Blueprint
from flask_restx import Api

recommendations_blueprint = Blueprint('recommendations_api', __name__, url_prefix='/recommendations-api')
api = Api(recommendations_blueprint, title='Recommendations API', description='Recommendations api', doc='/doc')
