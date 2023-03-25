from extensions.database_extension import db, BaseModel

class Alternative(db.Model, BaseModel):
    __tablename__ = 'alternatives'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.Text, nullable=False)
    score = db.Column(db.Integer, nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))

    def __init__(self, description, score, question_id):
        self.description = description
        self.score = score
        self.question_id = question_id
