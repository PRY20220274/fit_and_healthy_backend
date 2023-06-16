from domain.motivations.models.food_goal import FoodGoal
from domain.motivations.services.objective import get_objective
from domain.motivations.services.activity import get_activity
from domain.accounts.services.user import get_user_age
from domain.accounts.services.weight import get_last_weight
from extensions.exception_extension import BadRequestException


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


def get_calories(activity, user):
    genre = user.genre
    weight = get_last_weight(user.id);
    age = get_user_age(user)
    energy_expenditure = 0
    if age >= 18 and age <= 30:
        if user.genre == 'M':
            energy_expenditure = (15.057 * weight) + 692.2 
        elif user.genre == 'F':
            energy_expenditure = (14.818 * weight) + 486.6 
        else:
            energy_expenditure = 0
    elif age >= 31 and age <= 60:
        if user.genre == 'M':
            energy_expenditure = (11.472 * weight) + 873.1 
        elif user.genre == 'F':
            energy_expenditure = (8.126 * weight) + 845.6 
        else:
            energy_expenditure = 0
    elif age >= 60:
        if user.genre == 'M':
            energy_expenditure = (11.711 * weight) + 587.1 
        elif user.genre == 'F':
            energy_expenditure = (9.082 * weight) + 658.5
        else:
            energy_expenditure = 0
    else:
        energy_expenditure = 0
    caloric_expenditure = activity.factor * energy_expenditure
    return round(caloric_expenditure, 2)


def get_description(objective, calories):
    if objective.name == 'Engordar':
        calories = calories + 500
        response = f'La cantidad de calorías que necesita ingerir para ganar masa muscular es de {calories} calorías por día '
        return response
    elif objective.name == 'Adelgazar':
        calories = calories - 500
        response = f'La cantidad de calorías que esta mujer necesita ingerir para adelgazar es de {calories} calorías por día.'
        return response
    elif objective.name == 'Mantener':
        response = f'La cantidad de calorías que necesita consumir para mantener su peso actual es de {calories} calorías por día'
        return response
    else:
        return 'Debes consumir calorias'


def save_goal(user, objective, activity):
    calories = get_calories(activity, user)
    description = get_description(objective, calories)
    goal = FoodGoal(description)

    goal.user_id = user.id
    goal.objective_id = objective.id
    goal.activity_id = activity.id
    
    created = goal.save()
    created.commit()
    return created
