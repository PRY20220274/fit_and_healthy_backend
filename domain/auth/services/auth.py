import base64
import datetime
from flask import make_response
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token


def encrypt_data(data):
    token = base64.urlsafe_b64encode(data.encode())
    return token.decode('ascii')


def decrypt_data(token):
    data = base64.urlsafe_b64decode(token)
    return data.decode('ascii')


def check_password(value1, value2):
    response = check_password_hash(value1, value2)
    return response


def access_token(identity):
    response = create_access_token(identity=identity, expires_delta=datetime.timedelta(hours=5))
    return response

