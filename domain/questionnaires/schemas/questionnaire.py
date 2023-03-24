from extensions.database_extension import ma
from domain.questionnaires.models.questionnaire import Questionnaire
from domain.questionnaires.schemas.question import QuestionSchema

class QuestionnaireSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "start_hour", "end_hour", "category", "questions")
        model = Questionnaire

    category = ma.Method("get_category")
    questions = ma.Method("get_questions")

    def get_category(self, obj):
        category = obj.category 
        return category.name

    def get_questions(self, obj):
        questions = obj.questions
        schema = QuestionSchema(many=True)
        return schema.dump(questions)