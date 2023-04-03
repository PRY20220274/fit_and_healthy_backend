from flask import request
from flask_restx import Resource
from api.motivations.adapters.docs.physical_goal import physical_goal_namespace
from api.motivations.adapters.requests.physical_goal import physical_goal_request
from api.motivations.adapters.responses.physical_goal import physical_goal_response
from domain.motivations.schemas.physical_goal import PhysicalGoalSchema
from domain.motivations.services.physical_goal import get_goals_by_user, build_goal, save_goal
from domain.commons.util import get_user


@physical_goal_namespace.route('')
class PhysicalListResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.schemas = PhysicalGoalSchema(many=True)
        self.schema = PhysicalGoalSchema()

    @physical_goal_namespace.response(code=400, description='Bad Request')
    @physical_goal_namespace.marshal_list_with(physical_goal_response, code=200, description='Success')
    def get(self):
        user = get_user()
        goals = get_goals_by_user(user.id)
        response = self.schemas.dump(goals)
        return response, 200

    @physical_goal_namespace.expect(physical_goal_request)
    @physical_goal_namespace.response(code=400, description='Bad Request')
    @physical_goal_namespace.response(code=201, description='Success', model=physical_goal_response)
    def post(self):
        data, frequency = build_goal(request.get_json())
        body = self.schema.load(data)
        user = get_user()
        goal = save_goal(body, user, frequency)
        response = self.schema.dump(goal)
        return response, 201
