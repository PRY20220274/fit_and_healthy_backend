from extensions.database_extension import db, BaseModel
from sqlalchemy.dialects.mysql import TIME
from sqlalchemy.orm import backref

class Questionnaire(db.Model, BaseModel):
    __tablename__ = 'questionnaires'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    start_hour = db.Column(TIME(), nullable=False)
    end_hour = db.Column(TIME(), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('questionnaire_categories.id'))
    category = db.relationship("QuestionnaireCategory")
    questions = db.relationship("Question", secondary=lambda: questionnaries_questions, lazy='dynamic',
                                            backref=backref("questionnaires", lazy='dynamic'))

    def __init__(self, name, start_hour, end_hour, category_id):
        self.name = name
        self.start_hour = start_hour
        self.end_hour = end_hour
        self.category_id = category_id


questionnaries_questions = db.Table(
    'questionnaires_questions', 
    db.metadata,
    db.Column('questionnaire_id', db.ForeignKey('questionnaires.id'), primary_key=True),
    db.Column('question_id', db.ForeignKey('questions.id'), primary_key=True)
)