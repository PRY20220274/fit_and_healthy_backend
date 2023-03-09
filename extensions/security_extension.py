from flask_jwt_extended import JWTManager
from domain.accounts.services.user import get_user
jwt = JWTManager()


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    id = jwt_data["sub"]
    return get_user(id)


def register_security(app):

    jwt.init_app(app)