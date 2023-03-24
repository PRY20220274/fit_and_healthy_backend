from api.questionnaires.adapters.docs.solved_questionnaire import solved_namespace
from flask_restx import fields

detail_response = solved_namespace.model('SolvedQuestionnaireDetailResponse', {
    'id': fields.Integer,
    'question': fields.String,
    'alternative': fields.String,
    'score': fields.Integer
})

solved_request = solved_namespace.model('SolvedQuestionnaireRequest', {
    'id': fields.Integer,
    'score': fields.Integer,
    'details': fields.List(fields.Nested(detail_response), description='Lista de detalles')
})
