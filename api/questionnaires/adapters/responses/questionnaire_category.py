from api.questionnaires.adapters.docs.questionnaire_category import category_namespace
from flask_restx import fields


category_response = category_namespace.model('CategoryResponse', {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'icon': fields.String
})
