from extensions.database_extension import ma
from domain.questionnaires.models.question import Question

class QuestionSchema(ma.Schema):
    class Meta:
        fields = ("id", "description")
        model = Question
