from extensions.database_extension import db, BaseModel
from sqlalchemy.orm import backref

class Questionnaire(db.Model, BaseModel):
    __tablename__ = 'questionnaires'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('questionnaire_categories.id'))
    category = db.relationship("QuestionnaireCategory")
    frequency_id = db.Column(db.Integer, db.ForeignKey('frequency_food.id'))
    frequency = db.relationship("FrequencyFood")
    questions = db.relationship("Question", secondary=lambda: questionnaries_questions, lazy='dynamic',
                                            backref=backref("questionnaires", lazy='dynamic'))
    scales = db.relationship('Scale', lazy=True)                                        

    def __init__(self, name, frequency_id, category_id):
        self.name = name
        self.frequency_id = frequency_id
        self.category_id = category_id


questionnaries_questions = db.Table(
    'questionnaires_questions', 
    db.metadata,
    db.Column('questionnaire_id', db.ForeignKey('questionnaires.id'), primary_key=True),
    db.Column('question_id', db.ForeignKey('questions.id'), primary_key=True)
)