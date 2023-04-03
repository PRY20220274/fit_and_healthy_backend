from flask_cors import cross_origin
from flask_jwt_extended import jwt_required
from flask_restx import Namespace

objective_namespace = Namespace('objectives', description='Objectives operations', decorators=[cross_origin(), jwt_required()])
