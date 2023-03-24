from api.questionnaires.adapters.docs.solved_questionnaire import solved_namespace
from flask_restx import fields

solved_request = solved_namespace.model('SolvedQuestionnaireRequest', {
    'questionnaire': fields.Integer(required=True),
    'answers': fields.List(fields.Integer, required=True)
})
