from extensions.database_extension import db, BaseModel

class Recommendation(db.Model, BaseModel):
    __tablename__ = 'recommendations'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.Text, nullable=False)
    type = db.Column(db.String(200), nullable=False)


    __mapper_args__ = {
        'polymorphic_identity': 'recommendation',
        'polymorphic_on': type
    }

    def __init__(self, description, min, max):
        self.description = description
