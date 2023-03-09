from domain.motivations.models.goal import Goal
from domain.motivations.services.motivation_type import get_type
from domain.motivations.services.frequency import get_frequency
from extensions.exception_extension import NotFoundException

def get_goals_by_user(user_id):
    goals = Goal.simple_filter(**{'user_id': user_id})
    return goals

def clean_goal(data):
    frequency_id = data.get('frequency', None)
    type_id = data.get('type', None)
    del data['frequency']
    del data['type']
    return data, frequency_id, type_id

def save_goal(goal, user_id, frequency_id, type_id):
    goal.user_id = user_id

    if frequency_id is not None:
        if get_frequency(frequency_id):
            goal.frequency_id = frequency_id
    if type_id is not None:
        if get_type(type_id):
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
