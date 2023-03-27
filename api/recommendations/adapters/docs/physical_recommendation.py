from flask_cors import cross_origin
from flask_jwt_extended import jwt_required
from flask_restx import Namespace

physical_namespace = Namespace('physical', description='Physical Recommendations operations', decorators=[cross_origin(), jwt_required()])
