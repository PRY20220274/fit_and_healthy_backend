from extensions.database_extension import db, BaseModel
from domain.commons.util import get_datetime, format_date_to_save
from sqlalchemy.dialects.mysql import TIME

class Questionnaire(db.Model, BaseModel):
    __tablename__ = 'questionnaires'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    start_hour = db.Column(TIME(), nullable=False)
    end_hour = db.Column(TIME(), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('questionnaire_categories.id'))
    category = db.relationship("QuestionnaireCategory")

    def __init__(self, name, start_hour, end_hour, category_id):
        self.name = name
        self.start_hour = start_hour
        self.end_hour = end_hour
        self.category_id = category_id
