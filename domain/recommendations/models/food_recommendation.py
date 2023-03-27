from extensions.database_extension import db, BaseModel

class FoodRecommendation(db.Model, BaseModel):
    __tablename__ = 'food_recommendations'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.Text, nullable=False)
    min = db.Column(db.Integer, nullable=False)
    max = db.Column(db.Integer, nullable=False)
    frequency_id = db.Column(db.Integer, db.ForeignKey('frequency_food.id'))
    frequency = db.relationship("FrequencyFood")

    def __init__(self, description, min, max):
        self.description = description
        self.min = min
        self.max = max
