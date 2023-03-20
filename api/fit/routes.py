from flask import Blueprint
from flask_restx import Api
from api.fit.controllers.iot import iot_namespace
from api.fit.controllers.physical_data import physical_data_namespace

fit_blueprint = Blueprint('fit_api', __name__, url_prefix='/fit-api')
api = Api(fit_blueprint, title='Fit API', description='Fit api', doc='/doc')

api.add_namespace(iot_namespace)
api.add_namespace(physical_data_namespace)
