from domain.questionnaires.models.questionnaire_category import QuestionnaireCategory

def get_categories():
    categories = QuestionnaireCategory.get_all()
    return categories
