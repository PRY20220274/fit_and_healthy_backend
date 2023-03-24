from flask import request
from flask_restx import Resource
from api.questionnaires.adapters.docs.solved_questionnaire import solved_namespace
from api.questionnaires.adapters.requests.solved_questionnaire import solved_request
from api.questionnaires.adapters.responses.solved_questionnaire import solved_response
from domain.questionnaires.schemas.solved_questionnaire import SolvedQuestionnaireSchema
from domain.questionnaires.services.solved_questionnaire import build_questionnaire, save_solved
from domain.commons.util import get_user


@solved_namespace.route('')
class SolvedQuestionnaireResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.schema = SolvedQuestionnaireSchema()

    @solved_namespace.expect(solved_request)
    @solved_namespace.response(code=400, description='Bad Request')
    @solved_namespace.response(code=201, description='Success', model=solved_response)
    def post(self):
        questionnaire_id = build_questionnaire(request.get_json())
        user = get_user()
        solved = save_solved(user.id, questionnaire_id)
        response = self.schema.dump(solved)
        return response, 201
