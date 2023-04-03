from flask import request
from flask_restx import Resource
from api.motivations.adapters.docs.objective import objective_namespace
from api.motivations.adapters.responses.objective import objective_response
from domain.motivations.schemas.objective import ObjectiveSchema
from domain.motivations.services.objective import get_objectives

@objective_namespace.route('')
class ObjectiveListResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.schema = ObjectiveSchema(many=True)

    @objective_namespace.marshal_list_with(objective_response, code=200, description='Success')
    @objective_namespace.response(code=400, description='Bad Request')
    def get(self):
        objectives = get_objectives()
        response = self.schema.dump(objectives)
        return response, 200
