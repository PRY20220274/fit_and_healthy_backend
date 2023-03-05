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


def get_user():
    user = current_user
    return user