from domain.accounts.models.user import User
from domain.commons.util import get_variable, get_datetime
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
    user.weight = get_variable(data, 'weight', user.weight)
    user.height = get_variable(data, 'height', user.height)
    user.format_date()
    return user.update()
