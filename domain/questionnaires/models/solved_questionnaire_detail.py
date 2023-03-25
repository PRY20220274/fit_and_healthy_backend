from extensions.database_extension import db, BaseModel
from domain.commons.util import get_datetime

class SolvedQuestionnaireDetail(db.Model, BaseModel):
    __tablename__ = 'solved_questionnaire_details'

    solved_questionnaire_id = db.Column(db.Integer, db.ForeignKey('solved_questionnaires.id'), primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), primary_key=True)
    alternative_id = db.Column(db.Integer, db.ForeignKey('alternatives.id'), primary_key=True)
    solved_questionnaire = db.relationship("SolvedQuestionnaire", back_populates="details")
    question = db.relationship("Question")
    alternative = db.relationship("Alternative")

    def __init__(self, solved_questionnaire_id, question_id, alternative_id):
        self.solved_questionnaire_id = solved_questionnaire_id
        self.question_id = question_id
        self.alternative_id = alternative_id
