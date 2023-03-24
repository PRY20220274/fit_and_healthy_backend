from flask_jwt_extended import current_user
from datetime import datetime

def get_datetime():
    date = datetime.utcnow()
    return date

def format_date_to_save(date):
    date = datetime.strptime(date, "%d/%m/%Y").strftime("%Y-%m-%d")
    return date


def format_date_to_show(date):
    date = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
    return date


def format_datetime_to_show(date):
    date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S").strftime("%d/%m/%Y %H:%M:%S")
    return date


def get_user():
    user = current_user
    return user


def get_param(params, search):
    return params.get(search) if params.get(search) else None


def get_variable(data, search, default):
    return data.get(search) if data.get(search) else default


def get_fog():
    return 'http://localhost:4040/api'


def get_hour():
    now = datetime.now()
    actual_hour = now.strftime("%H:%M:%S")
    return actual_hour
