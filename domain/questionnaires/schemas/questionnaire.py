from extensions.database_extension import ma
from domain.questionnaires.models.questionnaire import Questionnaire
from domain.questionnaires.schemas.question import QuestionSchema

class QuestionnaireSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "frequency", "category", "questions")
        model = Questionnaire

    category = ma.Method("get_category")
    frequency = ma.Method("get_frequency")
    questions = ma.Method("get_questions")

    def get_category(self, obj):
        category = obj.category 
        return category.name

    def get_frequency(self, obj):
        frequency = obj.frequency 
        return frequency.name

    def get_questions(self, obj):
        questions = obj.questions
        schema = QuestionSchema(many=True)
        return schema.dump(questions)
        