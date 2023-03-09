from domain.motivations.models.motivation_type import MotivationType

def get_types():
    types = MotivationType.get_all()
    return types


def get_type(id):
    type = MotivationType.get_by_id(id)
    if type:
        return type
    else:
        raise NotFoundException('MotivationType', 'id', id)
