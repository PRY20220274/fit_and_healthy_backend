from flask_restx import Resource
from api.fit.adapters.docs.iot import iot_namespace
from api.fit.adapters.responses.iot import url_response, access_response
from domain.commons.util import get_fog
from domain.commons.responses import get_access
from restx import RestxClient
from restx.object_mapper import ObjectMapper

@iot_namespace.route('/authentication-url')
class AuthenticationUrlResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @iot_namespace.response(code=200, description='Success', model=url_response)
    @iot_namespace.response(code=400, description='Bad Request')
    def get(self):
        url = f'{get_fog()}/url'
        response = requests.get(url)
        data = response.json()
        return data


@iot_namespace.route('/access')
class AccessResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @iot_namespace.response(code=200, description='Success', model=access_response)
    @iot_namespace.response(code=400, description='Bad Request')
    def post(self):
        url = f'{get_fog()}/access'
        response = requests.get(url)
        data = response.json()
        return get_access()

