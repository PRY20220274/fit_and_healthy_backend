from domain.recommendations.models.recommendation import Recommendation
from extensions.database_extension import db

class FoodRecommendation(Recommendation):
    __tablename__ = 'food_recommendations'

    id = db.Column(db.Integer, db.ForeignKey('recommendations.id'), primary_key=True)
    min = db.Column(db.Integer, nullable=False)
    max = db.Column(db.Integer, nullable=False)
    frequency_id = db.Column(db.Integer, db.ForeignKey('frequency_food.id'))
    frequency = db.relationship("FrequencyFood")

    __mapper_args__ = {
        'polymorphic_identity': 'food_recommendation',
    }

    def __init__(self, description, min, max, frequency_id):
        self.description = description
        self.type = 'food_recommendation'
        self.min = min
        self.max = max
        self.frequency_id = frequency_id
