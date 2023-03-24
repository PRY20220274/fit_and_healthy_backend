from extensions.database_extension import ma
from domain.questionnaires.models.solved_questionnaire_detail import SolvedQuestionnaireDetail

class SolvedQuestionnaireDetailSchema(ma.Schema):
    class Meta:
        fields = ("question", "alternative", "score")
        model = SolvedQuestionnaireDetail

    question = ma.Method("get_question")
    alternative = ma.Method("get_alternative")
    score = ma.Method("get_score")

    def get_question(self, obj):
        question = obj.question 
        return question.description

    def get_alternative(self, obj):
        alternative = obj.alternative
        return alternative.description

    def get_score(self, obj):
        alternative = obj.alternative
        return alternative.score
