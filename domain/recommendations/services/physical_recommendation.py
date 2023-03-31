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


def get_recommendation(score):
    recommendation = PhysicalRecommendation.query.filter(
            score >= PhysicalRecommendation.min,
            score <= PhysicalRecommendation.max
    ).first()
    return recommendation


def add_recommendation_to_user(user_id, score):
    recommendation = get_recommendation(score)
    created = PhysicalUserRecommendation(user_id, recommendation.id)
    created.save()
    created.commit()
