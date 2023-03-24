from extensions.database_extension import ma
from domain.questionnaires.models.questionnaire_category import QuestionnaireCategory
from domain.questionnaires.models.question import Question

class QuestionnaireCategorySchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "description", "icon")
        model = QuestionnaireCategory
