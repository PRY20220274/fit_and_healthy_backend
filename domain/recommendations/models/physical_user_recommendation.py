from extensions.database_extension import db, BaseModel
from domain.commons.util import get_datetime

class PhysicalUserRecommendation(db.Model, BaseModel):
    __tablename__ = 'physical_recommendations_users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, nullable=False)
    physical_recommendation_id = db.Column(db.Integer, db.ForeignKey('physical_recommendations.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    physical_recommendation = db.relationship("PhysicalRecommendation")
    user = db.relationship("User")

    def __init__(self, user_id, physical_recommendation_id):
        self.user_id = user_id
        self.physical_recommendation_id = physical_recommendation_id
        self.created_at = get_datetime()
