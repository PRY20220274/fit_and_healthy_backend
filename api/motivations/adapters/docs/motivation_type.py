from flask_cors import cross_origin
from flask_jwt_extended import jwt_required
from flask_restx import Namespace

motivation_type_namespace = Namespace('types', description='Motivation Types operations', decorators=[cross_origin(), jwt_required()])
