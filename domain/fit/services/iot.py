from domain.fit.models.access import Access
from domain.fit.services.physical_data import create_physical_data
from domain.recommendations.services.physical_recommendation import add_recommendation_to_user

def save_access(data, user_id):
    exists = get_access_user(user_id)
    if not exists:
        access = create_access(data, user_id)
        created = access.save()
        created.commit()
        return True
    else:
        return False


def create_access(data, user_id):
    access = Access(
        data['access_token'], 
        data['refresh_token'], 
        data['scope'], 
        data['token_type'], 
        data['expiry_date']
    )
    access.user_id = user_id

    return access


def get_access_user(user_id):
    access = Access.get_one(**{'user_id': user_id})
    return access


def save_iot_data(data, user_id):
    physical_data = create_physical_data(data, user_id)
    created = physical_data.save()
    add_recommendation_to_user(user_id, created.calories)
    created.commit()
