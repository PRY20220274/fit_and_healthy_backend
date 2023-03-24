from api.questionnaires.adapters.docs.questionnaire import questionnaire_namespace
from flask_restx import fields


questionnaire_response = questionnaire_namespace.model('QuestionnarieResponse', {
    'id': fields.Integer,
    'name': fields.String,
    'start_hour': fields.String,
    'end_hour': fields.String,
    'category': fields.String
})
