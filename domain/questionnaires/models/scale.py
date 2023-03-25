from extensions.database_extension import db, BaseModel

class Scale(db.Model, BaseModel):
    __tablename__ = 'scales'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.Text, nullable=False)
    min = db.Column(db.Integer, nullable=False)
    max = db.Column(db.Integer, nullable=False)
    questionnaire_id = db.Column(db.Integer, db.ForeignKey('questionnaires.id'))

    def __init__(self, description, min, max, questionnaire_id):
        self.description = description
        self.min = min
        self.max = max
        self.questionnaire_id = questionnaire_id
