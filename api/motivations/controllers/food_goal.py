from flask import request
from flask_restx import Resource
from api.motivations.adapters.docs.food_goal import food_goal_namespace
from api.motivations.adapters.requests.food_goal import food_goal_request
from api.motivations.adapters.responses.food_goal import food_goal_response
from domain.motivations.schemas.food_goal import FoodGoalSchema
from domain.motivations.services.food_goal import get_goals_by_user, build_goal, save_goal
from domain.commons.util import get_user


@food_goal_namespace.route('')
class GoalListResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.schemas = FoodGoalSchema(many=True)
        self.schema = FoodGoalSchema()

    @food_goal_namespace.response(code=400, description='Bad Request')
    @food_goal_namespace.marshal_list_with(food_goal_response, code=200, description='Success')
    def get(self):
        user = get_user()
        goals = get_goals_by_user(user.id)
        response = self.schemas.dump(goals)
        return response, 200

    @food_goal_namespace.expect(food_goal_request)
    @food_goal_namespace.response(code=400, description='Bad Request')
    @food_goal_namespace.response(code=201, description='Success', model=food_goal_response)
    def post(self):
        objective, activity = build_goal(request.get_json())
        user = get_user()
        goal = save_goal(user.id, objective.id, activity.id)
        response = self.schema.dump(goal)
        return response, 201
