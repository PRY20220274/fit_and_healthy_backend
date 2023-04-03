from domain.recommendations.models.recommendation import Recommendation
from extensions.database_extension import db

class PhysicalRecommendation(Recommendation):
    __tablename__ = 'physical_recommendations'

    id = db.Column(db.Integer, db.ForeignKey('recommendations.id'), primary_key=True)
    min_calories = db.Column(db.Integer, nullable=False)
    max_calories = db.Column(db.Integer, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'physical_recommendation',
    }

    def __init__(self, description, min_calories, max_calories):
        self.description = description
        self.type = 'physical_recommendation'
        self.min_calories = min_calories
        self.max_calories = max_calories
