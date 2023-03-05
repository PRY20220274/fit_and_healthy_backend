from api.accounts.adapters.docs.user import user_namespace
from flask_restx import fields


user_response = user_namespace.model('UserResponse', {
    'id': fields.Integer,
    'email': fields.String,
    'first_name': fields.String,
    'last_name': fields.String,
    'birth_date': fields.String
})
