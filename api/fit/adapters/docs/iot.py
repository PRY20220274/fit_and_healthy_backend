from flask_cors import cross_origin
from flask_jwt_extended import jwt_required
from flask_restx import Namespace

iot_namespace = Namespace('iot', description='IOT operations', decorators=[cross_origin(), jwt_required()])

