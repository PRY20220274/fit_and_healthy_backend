from domain.accounts.models.weight import Weight
from domain.commons.util import get_date

def get_last_weight(user_id):
    weight = Weight.query.filter(
        Weight.user_id == user_id
    ).order_by(Weight.created_at.desc()).first()
    return weight


def get_user_weight(user_id):
    weights = Weight.query.filter(
        Weight.user_id == user_id
    )
    return weights