from flask import request
from flask_restx import Resource
from api.motivations.adapters.docs.frequency import frequency_namespace
from api.motivations.adapters.responses.frequency import frequency_response
from domain.motivations.schemas.frequency import FrequencySchema
from domain.motivations.services.frequency import get_frequencies

@frequency_namespace.route('')
class FrequencyListResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.schema = FrequencySchema(many=True)

    @frequency_namespace.marshal_list_with(frequency_response, code=200, description='Success')
    @frequency_namespace.response(code=400, description='Bad Request')
    def get(self):
        frequencies = get_frequencies()
        response = self.schema.dump(frequencies)
        return response, 200
