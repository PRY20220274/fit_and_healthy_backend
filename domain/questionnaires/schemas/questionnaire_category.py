from extensions.database_extension import ma
from marshmallow import post_dump
from domain.questionnaires.models.questionnaire_category import QuestionnaireCategory
from domain.commons.util import format_datetime_to_show

class QuestionnaireCategorySchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "description", "icon")
        model = QuestionnaireCategory
