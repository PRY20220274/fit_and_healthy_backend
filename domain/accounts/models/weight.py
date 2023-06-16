from extensions.database_extension import db, BaseModel
from domain.commons.util import get_datetime

class Weight(db.Model, BaseModel):
    __tablename__ = 'weights'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    value = db.Column(db.Float)
    created_at = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User")

    def __init__(self, value):
        self.value = value
        self.created_at = get_datetime()
