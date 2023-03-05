from flask_jwt_extended import JWTManager
from domain.accounts.services.user import find_user
jwt = JWTManager()


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    id = jwt_data["sub"]
    return find_user(id)


def register_security(app):

    jwt.init_app(app)