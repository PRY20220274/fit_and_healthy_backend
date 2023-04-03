from flask import request
from flask_restx import Resource
from api.motivations.adapters.docs.goal import goal_namespace
from api.motivations.adapters.responses.goal import goal_response
from domain.commons.responses import goal_completed
from domain.motivations.services.goal import get_goal, complete_goal


@goal_namespace.route('/<int:goal_id>/completed')
class GoalDetailResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @goal_namespace.response(code=200, description='Success', model=goal_response)
    @goal_namespace.response(code=404, description='Goal not found')
    def patch(self, goal_id):
        goal = get_goal(goal_id)
        complete_goal(goal)
        return goal_completed()