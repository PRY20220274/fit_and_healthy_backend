from flask import Blueprint
from flask_restx import Api

fit_blueprint = Blueprint('fit_api', __name__, url_prefix='/fit-api')
api = Api(fit_blueprint, title='Fit API', description='Fit api', doc='/doc')
