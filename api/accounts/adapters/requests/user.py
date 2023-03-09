from api.accounts.adapters.docs.user import user_namespace
from flask_restx import fields

user_request = user_namespace.model('UserRequest', {
    'first_name': fields.String,
    'last_name': fields.String,
    'birth_date': fields.String
})
