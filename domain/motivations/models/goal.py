from extensions.database_extension import db, BaseModel
from domain.commons.util import get_datetime, format_date_to_save

class Goal(db.Model, BaseModel):
    __tablename__ = 'goals'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('motivation_types.id'))
    type = db.relationship("MotivationType")
    frequency_id = db.Column(db.Integer, db.ForeignKey('frequencies.id'))
    frequency = db.relationship("Frequency")
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User")

    def __init__(self, description):
        self.description = description
        self.created_at = get_datetime()
