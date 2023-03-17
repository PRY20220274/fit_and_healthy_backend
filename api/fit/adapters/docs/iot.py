from flask_cors import cross_origin
from flask_restx import Namespace

iot_namespace = Namespace('iot', description='IOT operations', decorators=[cross_origin()])
