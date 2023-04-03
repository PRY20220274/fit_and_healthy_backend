from flask_cors import cross_origin
from flask_jwt_extended import jwt_required
from flask_restx import Namespace

food_goal_namespace = Namespace('food-goals', description='Food Goals operations', 
                                decorators=[cross_origin(), jwt_required()])
