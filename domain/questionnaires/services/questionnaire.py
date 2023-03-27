from domain.questionnaires.models.questionnaire import Questionnaire
from domain.recommendations.models.frequency_food import FrequencyFood
from domain.questionnaires.models.solved_questionnaire import SolvedQuestionnaire
from domain.commons.util import get_hour, get_date
from extensions.exception_extension import NotFoundException


def get_questionnaire_by_category(category_id):
    hour = get_hour()
    questionnaire = Questionnaire.query.filter(
        Questionnaire.category_id == category_id
    ).join(FrequencyFood).filter(        
        hour > FrequencyFood.start_hour, 
        hour < FrequencyFood.end_hour
    ).first()
    return questionnaire


def get_questionnaire(id):
    questionnaire = Questionnaire.get_by_id(id)
    if questionnaire:
        return questionnaire
    else:
        raise NotFoundException('questionnaire', 'id', id)


def get_last_solved(user_id):
    solved = SolvedQuestionnaire.query.filter_by(user_id=user_id).order_by(SolvedQuestionnaire.created_at.desc()).first()
    return solved


def get_actual_frequency():
    hour = get_hour()
    frequency = FrequencyFood.query.filter(
        hour > FrequencyFood.start_hour, 
        hour < FrequencyFood.end_hour
        ).first()
    return frequency


def is_enable(user):
    last_solved = get_last_solved(user.id)
    last_solved_date = last_solved.created_at.strftime("%Y-%m-%d")
    last_solved_frequency = last_solved.questionnaire.frequency

    date = get_date()
    if last_solved_date != date:
        return True
    
    actual_frequency = get_actual_frequency()

    if actual_frequency.id == last_solved_frequency.id:
        return False
    
    return True
