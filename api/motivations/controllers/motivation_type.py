from flask import request
from flask_restx import Resource
from api.motivations.adapters.docs.motivation_type import motivation_type_namespace
from api.motivations.adapters.responses.motivation_type import motivation_type_response
from domain.motivations.schemas.motivation_type import MotivationTypeSchema
from domain.motivations.services.motivation_type import get_types

@motivation_type_namespace.route('')
class MotivationTypeListResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.schema = MotivationTypeSchema(many=True)

    @motivation_type_namespace.marshal_list_with(motivation_type_response, code=200, description='Success')
    @motivation_type_namespace.response(code=400, description='Bad Request')
    def get(self):
        types = get_types()
        response = self.schema.dump(types)
        return response, 200
