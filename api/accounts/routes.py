from flask import Blueprint
from flask_restx import Api
from api.accounts.controllers.user import user_namespace

accounts_blueprint = Blueprint('accounts_api', __name__, url_prefix='/accounts-api')
api = Api(accounts_blueprint, title='Accounts API', description='Accounts api', doc='/doc')

api.add_namespace(user_namespace)
