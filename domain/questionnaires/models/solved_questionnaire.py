from extensions.database_extension import db, BaseModel
from domain.commons.util import get_datetime

class SolvedQuestionnaire(db.Model, BaseModel):
    __tablename__ = 'solved_questionnaires'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    score = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    questionnaire_id = db.Column(db.Integer, db.ForeignKey('questionnaires.id'))
    questionnaire = db.relationship("Questionnaire")
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User")

    def __init__(self, score, created_at):
        self.score = score
        self.created_at = get_datetime()
