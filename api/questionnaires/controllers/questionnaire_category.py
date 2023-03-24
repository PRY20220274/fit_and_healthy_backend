from flask import request
from flask_restx import Resource
from api.questionnaires.adapters.docs.questionnaire_category import category_namespace
from api.questionnaires.adapters.responses.questionnaire_category import category_response
from domain.questionnaires.schemas.questionnaire_category import QuestionnaireCategorySchema
from domain.questionnaires.services.questionnaire_category import get_categories

@category_namespace.route('')
class CategoryListResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.schema = QuestionnaireCategorySchema(many=True)

    @category_namespace.marshal_list_with(category_response, code=200, description='Success')
    @category_namespace.response(code=400, description='Bad Request')
    def get(self):
        categories = get_categories()
        response = self.schema.dump(categories)
        return response, 200
