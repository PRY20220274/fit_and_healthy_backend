from extensions.database_extension import db, BaseModel
from domain.commons.util import get_datetime

class Objective(db.Model, BaseModel):
    __tablename__ = 'objectives'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, name):
        self.name = name
        self.created_at = get_datetime()
