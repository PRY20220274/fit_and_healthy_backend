from extensions.database_extension import db, BaseModel
from domain.commons.util import get_datetime, format_date_to_save

class Phrase(db.Model, BaseModel):
    __tablename__ = 'phrases'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    icon = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('motivation_types.id'))
    type = db.relationship("MotivationType")

    def __init__(self, title, icon, type_id):
        self.title = title
        self.icon = icon
        self.type_id = type_id
        self.created_at = get_datetime()
