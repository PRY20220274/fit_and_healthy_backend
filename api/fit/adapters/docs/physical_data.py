from flask_cors import cross_origin
from flask_jwt_extended import jwt_required
from flask_restx import Namespace

physical_data_namespace = Namespace('physical-data', 
                                    description='Physical Data operations', 
                                    decorators=[cross_origin(), jwt_required()])

