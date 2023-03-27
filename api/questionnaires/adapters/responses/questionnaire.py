from api.questionnaires.adapters.docs.questionnaire import questionnaire_namespace
from flask_restx import fields

alternative_response = questionnaire_namespace.model('AlternativeResponse', {
    'id': fields.Integer,
    'description': fields.String,
    'score': fields.Integer
})

question_response = questionnaire_namespace.model('QuestionResponse', {
    'id': fields.Integer,
    'description': fields.String,
    'alternatives': fields.List(fields.Nested(alternative_response))
})

questionnaire_response = questionnaire_namespace.model('QuestionnarieResponse', {
    'id': fields.Integer,
    'name': fields.String,
    'category': fields.String,
    'questions': fields.List(fields.Nested(question_response), description='Lista de preguntas')
})
