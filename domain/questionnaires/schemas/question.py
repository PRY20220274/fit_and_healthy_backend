from extensions.database_extension import ma
from domain.questionnaires.models.question import Question
from domain.questionnaires.schemas.alternative import AlternativeSchema

class QuestionSchema(ma.Schema):
    class Meta:
        fields = ("id", "description", "alternatives")
        model = Question

    alternatives = ma.Method("get_alternatives")

    def get_alternatives(self, obj):
        alternatives = obj.alternatives
        schema = AlternativeSchema(many=True)
        return schema.dump(alternatives)
