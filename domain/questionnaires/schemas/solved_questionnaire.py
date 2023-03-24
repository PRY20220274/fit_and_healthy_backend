from extensions.database_extension import ma
from domain.questionnaires.models.solved_questionnaire import SolvedQuestionnaire
from domain.questionnaires.schemas.solved_questionnaire_detail import SolvedQuestionnaireDetailSchema

class SolvedQuestionnaireSchema(ma.Schema):
    class Meta:
        fields = ("id", "score", "details")
        model = SolvedQuestionnaire

    details = ma.Method("get_details")

    def get_details(self, obj):
        details = obj.details
        schema = SolvedQuestionnaireDetailSchema(many=True)
        return schema.dump(details)
