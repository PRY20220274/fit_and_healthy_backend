from flask_restx import Resource
from api.fit.adapters.docs.physical_data import physical_data_namespace
from api.fit.adapters.responses.physical_data import physical_data_response
from domain.commons.util import get_user
from domain.fit.schemas.physical_data import PhysicalDataSchema
from domain.fit.services.physical_data import get_physical_data_user

@physical_data_namespace.route('')
class PhysicalDataResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.schema = PhysicalDataSchema()

    @physical_data_namespace.response(code=200, description='Success', model=physical_data_response)
    @physical_data_namespace.response(code=400, description='Bad Request')
    def get(self):
        user = get_user()
        physical_data = get_physical_data_user(user.id)
        response = self.schema.dump(physical_data)
        return response, 200

