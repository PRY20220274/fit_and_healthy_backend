from flask import request
from flask_restx import Resource
from api.motivations.adapters.docs.activity import activity_namespace
from api.motivations.adapters.responses.activity import activity_response
from domain.motivations.schemas.activity import ActivitySchema
from domain.motivations.services.activity import get_activities

@activity_namespace.route('')
class ActivityListResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.schema = ActivitySchema(many=True)

    @activity_namespace.marshal_list_with(activity_response, code=200, description='Success')
    @activity_namespace.response(code=400, description='Bad Request')
    def get(self):
        activities = get_activities()
        response = self.schema.dump(activities)
        return response, 200
