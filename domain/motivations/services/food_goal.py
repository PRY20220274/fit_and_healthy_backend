from domain.motivations.models.food_goal import FoodGoal
from domain.motivations.services.objective import get_objective
from domain.motivations.services.activity import get_activity
from extensions.exception_extension import NotFoundException, BadRequestException


def get_goals_by_user(user_id):
    goals = FoodGoal.simple_filter(**{'user_id': user_id})
    return goals


def build_goal(data):
    errors = {}
    objective_id = data.get('objective', None)
    activity_id = data.get('activity', None)
    objective = None
    activity = None


    if objective_id is not None:
        objective = get_objective(objective_id)
    else:
        errors['objective'] = 'Objective is required'
    
    if activity_id is not None:
        activity = get_activity(activity_id)
    else:
        errors['activity'] = 'Activity is required'

    if errors:
        raise BadRequestException(errors)

    return objective, activity


def save_goal(user_id, objective_id, activity_id):
    
    goal = FoodGoal('holi', 'food_goal')
    print('HERE', flush=True)
    print(goal, flush=True)
    goal.user_id = user_id
    goal.objective_id = objective_id
    goal.activity_id = activity_id
    created = goal.save()
    created.commit()
    return created
