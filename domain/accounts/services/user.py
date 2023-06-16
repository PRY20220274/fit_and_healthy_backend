from domain.accounts.models.user import User
from domain.accounts.models.weight import Weight
from domain.commons.util import get_variable, get_datetime
from domain.accounts.services.weight import get_last_weight
from extensions.exception_extension import NotFoundException

def get_user(id):
    user = User.get_by_id(id)
    if user:
        return user
    else:
        raise NotFoundException('user', 'id', id)

def get_user_email(email):
    user = User.get_one(**{'email': email})
    return user

def get_user_age(user):
    birth_date = user.birth_date
    today = get_datetime().date()
    age = (today - birth_date).days // 365.25
    return age

def update_user(user, data):
    user.first_name = get_variable(data, 'first_name', user.first_name)
    user.last_name = get_variable(data, 'last_name', user.last_name)
    user.birth_date = get_variable(data, 'birth_date', user.birth_date)
    user.height = get_variable(data, 'height', user.height)
    user.format_date()
    update_weight(data, user_id)
    return user.update()

def update_weight(data, user_id):
    value = data.get('weight')
    if value:
        last_user_weight = get_last_weight(user_id)
        if last_user_weight:
            if last_user_weight.value != value:
                weight = Weight(value)
                weight.user_id = user_id
                weight.save()
        elif not last_user_weight:
            weight = Weight(value)
            weight.user_id = user_id
            weight.save()