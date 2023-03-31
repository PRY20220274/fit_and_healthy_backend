from extensions.database_extension import db, BaseModel
from domain.commons.util import get_datetime

class FoodUserRecommendation(db.Model, BaseModel):
    __tablename__ = 'food_recommendations_users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, nullable=False)
    food_recommendation_id = db.Column(db.Integer, db.ForeignKey('food_recommendations.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    food_recommendation = db.relationship("FoodRecommendation")
    user = db.relationship("User")

    def __init__(self, user_id, food_recommendation_id):
        self.user_id = user_id
        self.food_recommendation_id = food_recommendation_id
        self.created_at = get_datetime()
