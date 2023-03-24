from extensions.database_extension import db, BaseModel

class Question(db.Model, BaseModel):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.Text, nullable=False)
    alternatives = db.relationship('Alternative', backref='question', lazy=True)

    def __init__(self, description):
        self.description = description
