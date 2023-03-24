from extensions.database_extension import db, BaseModel

class Alternative(db.Model, BaseModel):
    __tablename__ = 'alternatives'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.Text, nullable=False)
    score = db.Column(db.Integer, nullable=False)

    def __init__(self, description, score):
        self.description = description
        self.score = score
