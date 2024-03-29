from flask import request
from flask_restx import Resource
from api.accounts.adapters.docs.user import user_namespace
from api.accounts.adapters.responses.user import user_response, weight_response
from api.accounts.adapters.requests.user import user_request
from domain.accounts.schemas.user import UserSchema
from domain.accounts.schemas.weight import WeightSchema
from domain.accounts.services.user import update_user
from domain.accounts.services.weight import get_user_weight
from domain.commons.util import get_user

@user_namespace.route('/id')
class UserDetailResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.schema = UserSchema()

    @user_namespace.response(code=200, description='Success', model=user_response)
    @user_namespace.response(code=404, description='User not found')
    def get(self):
        user = get_user()
        response = self.schema.dump(user)
        return response, 200

    @user_namespace.expect(user_request)
    @user_namespace.response(code=200, description='Success', model=user_response)
    @user_namespace.response(code=404, description='Doctor not found')
    def patch(self):
        data = request.get_json()
        user = update_user(get_user(), data)
        response = self.schema.dump(user)
        return response, 200
    

@user_namespace.route('/weights')
class WeightListResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.schema = WeightSchema(many=True)

    @user_namespace.response(code=200, description='Success', model=weight_response)
    @user_namespace.response(code=404, description='User not found')
    def get(self):
        user = get_user()
        weights = get_user_weight(user.id)
        response = self.schema.dump(weights)
        return response, 200
