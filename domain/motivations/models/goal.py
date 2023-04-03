from extensions.database_extension import db, BaseModel
from sqlalchemy import case
from domain.commons.util import get_datetime

class Goal(db.Model, BaseModel):
    __tablename__ = 'goals'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User")
    type = db.Column(db.String(200), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'goal',
        'polymorphic_on': type
    }

    def __init__(self, description, type):
        self.description = description
        self.type = type
        self.created_at = get_datetime()
