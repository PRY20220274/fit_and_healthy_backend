from domain.motivations.models.activity import Activity

def get_activities():
    activities = Activity.get_all()
    return activities


def get_activity(id):
    activity = Activity.get_by_id(id)
    if activity:
        return activity
    else:
        raise NotFoundException('Activity', 'id', id)
