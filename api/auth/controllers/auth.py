from flask import request
from flask_restx import Resource
from api.auth.adapters.docs.auth import auth_namespace
from api.auth.adapters.requests.auth import login_request, register_request
from api.auth.adapters.responses.auth import login_response, login_unauthorized, register_response
from domain.auth.services.auth import check_password, access_token
from domain.accounts.services.user import get_user_email
from domain.auth.schemas.auth import LoginSchema, RegisterSchema
from domain.commons.responses import get_token, user_not_found, wrong_credentials, user_exists


@auth_namespace.route('/login')
class LoginResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.schema = LoginSchema()

    @auth_namespace.expect(login_request)
    @auth_namespace.response(code=200, description='Success', model=login_response)
    @auth_namespace.response(code=401, description='Unauthorized', model=login_unauthorized)
    def post(self):
        data = self.schema.load(request.get_json())
        email = data.get('email')
        password = data.get('password')
        user = get_user_email(email)
        if not user:
            return user_not_found()
        if check_password(user.password, password):
            token = access_token(user.id)
            return get_token(token)
        return wrong_credentials()


@auth_namespace.route('/register')
class RegisterResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.schema = RegisterSchema()

    @auth_namespace.expect(register_request)
    @auth_namespace.response(code=400, description='Bad Request')
    @auth_namespace.response(code=200, description='Success', model=register_response)
    def post(self):
        data = request.get_json()
        email = data.get('email')
        user = get_user_email(email)
        if not user:
            user = self.schema.load(data)
            result = self.schema.dump(user.save())
            return result, 201
        else:
            return user_exists()
