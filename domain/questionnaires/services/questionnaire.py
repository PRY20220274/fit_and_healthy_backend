from domain.questionnaires.models.questionnaire import Questionnaire
from domain.commons.util import get_hour

def get_questionnaire_by_category(category_id):
    hour = get_hour()
    questionnaire = Questionnaire.query.filter(
        hour > Questionnaire.start_hour, 
        hour < Questionnaire.end_hour,
        Questionnaire.category_id == category_id
    ).first()
    return questionnaire

def get_questionnaire(id):
    questionnaire = Questionnaire.get_by_id(id)
    if questionnaire:
        return questionnaire
    else:
        raise NotFoundException('questionnaire', 'id', id)
