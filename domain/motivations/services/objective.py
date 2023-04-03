from domain.motivations.models.objective import Objective

def get_objectives():
    objectives = Objective.get_all()
    return objectives


def get_objective(id):
    objective = Objective.get_by_id(id)
    if objective:
        return objective
    else:
        raise NotFoundException('Objective', 'id', id)
