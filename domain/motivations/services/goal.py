from domain.motivations.models.goal import Goal
from domain.motivations.services.motivation_type import get_type
from domain.motivations.services.frequency import get_frequency
from extensions.exception_extension import NotFoundException, BadRequestException

def get_goals_by_user(user_id):
    goals = Goal.simple_filter(**{'user_id': user_id})
    return goals

def clean_goal(data):
    errors = {}
    frequency_id = data.get('frequency', None)
    type_id = data.get('type', None)
    frequency = None
    type = None


    if frequency_id is not None:
        frequency = get_frequency(questionnaire_id)
    else:
        errors['frequency'] = 'Frequency is required'
    
    if type_id is not None:
        type = get_type(type_id)
    else:
        errors['type'] = 'Type is required'

    if errors:
        raise BadRequestException(errors)

    del data['frequency']
    del data['type']
    
    return data, frequency, type_id

def save_goal(goal, user_id, frequency_id, type_id):
    goal.user_id = user_id
    goal.frequency_id = frequency_id
    goal.type_id = type_id
    created = goal.save()
    created.commit()
    return created


def get_goal(id):
    goal = Goal.get_by_id(id)
    if goal:
        return goal
    else:
        raise NotFoundException('goal', 'id', id)
