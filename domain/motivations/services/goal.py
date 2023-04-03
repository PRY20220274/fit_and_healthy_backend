from domain.motivations.models.goal import Goal

def get_goal(id):
    goal = Goal.get_by_id(id)
    if goal:
        return goal
    else:
        raise NotFoundException('Goal', 'id', id)


def complete_goal(goal):
    goal.completed = True
    return goal.update()
