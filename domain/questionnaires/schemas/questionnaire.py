from extensions.database_extension import ma
from marshmallow import post_dump
from domain.questionnaires.models.questionnaire_category import QuestionnaireCategory
from domain.questionnaires.models.questionnaire import Questionnaire
from domain.commons.util import format_datetime_to_show

class QuestionnaireSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "start_hour", "end_hour", "category")
        model = Questionnaire

    category = ma.Method("get_category")

    def get_category(self, obj):
        category = obj.category 
        return category.name
