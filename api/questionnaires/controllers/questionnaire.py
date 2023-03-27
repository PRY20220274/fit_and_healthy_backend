from flask import request
from flask_restx import Resource
from domain.commons.util import get_param
from api.questionnaires.adapters.docs.questionnaire import questionnaire_namespace
from api.questionnaires.adapters.responses.questionnaire import questionnaire_response
from domain.questionnaires.schemas.questionnaire import QuestionnaireSchema
from domain.questionnaires.services.questionnaire import get_questionnaire_by_category, is_enable
from domain.commons.util import get_user
from domain.commons.responses import questionnaire_not_enable

@questionnaire_namespace.route('')
@questionnaire_namespace.doc(params={'category_id': 'Category Id'})
class QuestionnaireSearchResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.schema = QuestionnaireSchema()

    @questionnaire_namespace.response(code=201, description='Success', model=questionnaire_response)
    @questionnaire_namespace.response(code=400, description='Bad Request')
    def get(self):
        user = get_user()
        params = request.args
        category_id = get_param(params, 'category_id')
        enable = is_enable(user)
        print(enable, flush=True)
        if enable:
            questionnaire = get_questionnaire_by_category(category_id)
            response = self.schema.dump(questionnaire)
            return response, 200
        else:
            return questionnaire_not_enable()
