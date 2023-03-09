from domain.accounts.models.user import User
from extensions.exception_extension import NotFoundException


def get_param(params, search):
    return int(params.get(search)) if params.get(search) else None

def get_variable(data, search, default):
    return data.get(search) if data.get(search) else default

def get_user(id):
    user = User.get_by_id(id)
    if user:
        return user
    else:
        raise NotFoundException('user', 'id', id)

def get_user_email(email):
    user = User.get_one(**{'email': email})
    return user
