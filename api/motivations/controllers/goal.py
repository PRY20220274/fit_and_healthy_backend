from flask import request
from flask_restx import Resource
from api.motivations.adapters.docs.goal import goal_namespace
from api.motivations.adapters.requests.goal import goal_request
from api.motivations.adapters.responses.goal import goal_response
from domain.motivations.schemas.goal import GoalSchema
from domain.motivations.services.goal import get_goals_by_user, clean_goal, save_goal, get_goal
from domain.commons.util import get_user

@goal_namespace.route('')
@goal_namespace.doc(params={'user': 'User Id'})
class GoalListResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.schemas = GoalSchema(many=True)
        self.schema = GoalSchema()

    @goal_namespace.response(code=400, description='Bad Request')
    @goal_namespace.marshal_list_with(goal_response, code=200, description='Success')
    def get(self):
        user = get_user()
        goals = get_goals_by_user(user.id)
        response = self.schemas.dump(goals)
        return response, 200

    @goal_namespace.expect(goal_request)
    @goal_namespace.response(code=400, description='Bad Request')
    @goal_namespace.response(code=201, description='Success', model=goal_response)
    @goal_namespace.doc(params={'temperature_id': 'Temperature Id'})
    @goal_namespace.doc(params={'oxygen_id': 'Oxygen Id'})
    def post(self):
        data, frequency_id, type_id = clean_goal(request.get_json())
        body = self.schema.load(data)
        user = get_user()
        goal = save_goal(body, user.id, frequency_id, type_id)
        response = self.schema.dump(goal)
        return response, 201


@goal_namespace.route('/<int:id>')
class GoalDetailResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.schema = GoalSchema()

    @goal_namespace.response(code=200, description='Success', model=goal_response)
    @goal_namespace.response(code=400, description='Bad Request')
    def get(self, id):
        goal = get_goal(id)
        response = self.schema.dump(goal)
        return response, 200
