from extensions.database_extension import ma
from domain.questionnaires.models.solved_questionnaire import SolvedQuestionnaire
from domain.questionnaires.schemas.solved_questionnaire_detail import SolvedQuestionnaireDetailSchema

class SolvedQuestionnaireSchema(ma.Schema):
    class Meta:
        fields = ("id", "score", "details", "scale")
        model = SolvedQuestionnaire

    details = ma.Method("get_details")
    scale = ma.Method("get_scale")


    def get_details(self, obj):
        details = obj.details
        schema = SolvedQuestionnaireDetailSchema(many=True)
        return schema.dump(details)
    
    def get_scale(self, obj):
        questionnaire = obj.questionnaire
        scales = questionnaire.scales
        description = ''
        for scale in scales:
            if obj.score >= scale.min and obj.score <= scale.max:
                description = scale.description
        return description
