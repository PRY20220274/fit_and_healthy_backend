from flask import request
from flask_restx import Resource
from api.accounts.adapters.docs.user import user_namespace
from api.accounts.adapters.responses.user import user_response
from domain.accounts.schemas.user import UserSchema
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
