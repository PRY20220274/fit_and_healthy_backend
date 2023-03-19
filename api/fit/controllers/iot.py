from flask import request
import requests
from flask_restx import Resource
from api.fit.adapters.docs.iot import iot_namespace
from api.fit.adapters.requests.iot import access_request
from api.fit.adapters.responses.iot import url_response, access_response, iot_response
from domain.commons.util import get_fog, get_user
from domain.commons.responses import access_saved, access_denied, existing_access, blocked_information, iot_data_saved
from domain.fit.services.iot import save_access, get_access_user, save_iot_data

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

    @iot_namespace.expect(access_request)
    @iot_namespace.response(code=200, description='Success', model=access_response)
    @iot_namespace.response(code=400, description='Bad Request')
    def post(self):
        user = get_user()
        data = request.get_json()
        url = f'{get_fog()}/access'
        response = requests.post(url, json=data)
        if response.status_code == 200:
            verify = save_access(response.json(), user.id)
            if verify:
                return access_saved()
            else:
                return existing_access()
        else:
            return access_denied()


@iot_namespace.route('/data')
class IotResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @iot_namespace.response(code=200, description='Success', model=iot_response)
    @iot_namespace.response(code=400, description='Bad Request')
    def get(self):
        user = get_user()
        access = get_access_user(user.id)
        url = f'{get_fog()}/fit'
        response = requests.post(url, json=access.to_dict())
        print(response, flush=True)
        if response.status_code == 200:
            save_iot_data(response.json(), user.id)
            return iot_data_saved()
        else:
            return blocked_information()
