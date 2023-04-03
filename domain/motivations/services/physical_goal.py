from domain.motivations.models.physical_goal import PhysicalGoal
from domain.motivations.services.frequency import get_frequency
from extensions.exception_extension import BadRequestException


def get_goals_by_user(user_id):
    goals = PhysicalGoal.simple_filter(**{'user_id': user_id})
    return goals


def build_goal(data):
    errors = {}
    frequency_id = data.get('frequency', None)
    frequency = None

    if frequency_id is not None:
        frequency = get_frequency(frequency_id)
    else:
        errors['frequency'] = 'Frequency is required'

    if errors:
        raise BadRequestException(errors)

    del data['frequency']
    return data, frequency


def get_description(goal, frequency):
    response = f'Vas a realizar {goal.steps} pasos, {goal.kilometers} kilometros, con {goal.calories} consumidas en una frecuencia {frequency.name}'
    return response


def save_goal(goal, user, frequency):
    description = get_description(goal, frequency)
    goal.description = description
    goal.user_id = user.id
    goal.frequency_id = frequency.id
    
    created = goal.save()
    created.commit()
    return created
