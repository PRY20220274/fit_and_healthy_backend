from domain.motivations.models.motivation_type import MotivationType

def get_types():
    types = MotivationType.get_all()
    return types
