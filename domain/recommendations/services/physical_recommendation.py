from domain.recommendations.models.physical_recommendation import PhysicalRecommendation
from domain.recommendations.models.physical_user_recommendation import PhysicalUserRecommendation

def get_recommendations_by_user(user_id):
    recommendations = PhysicalRecommendation.query.join(PhysicalUserRecommendation).filter(
        user_id == PhysicalUserRecommendation.user_id
    ).distinct(PhysicalRecommendation.id)
    return recommendations


def get_today_recommendation(user_id):
    recommendation = PhysicalRecommendation.query.join(PhysicalUserRecommendation).filter(
            user_id == PhysicalUserRecommendation.user_id
    ).order_by(PhysicalUserRecommendation.created_at.desc()).first()
    return recommendation
