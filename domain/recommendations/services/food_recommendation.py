from domain.recommendations.models.food_recommendation import FoodRecommendation
from domain.recommendations.models.food_user_recommendation import FoodUserRecommendation
from domain.questionnaires.models.solved_questionnaire import SolvedQuestionnaire
from domain.questionnaires.models.questionnaire import Questionnaire
from domain.commons.util import get_date

def get_recommendations_by_user(user_id):
    recommendations = FoodRecommendation.query.join(FoodUserRecommendation).filter(
        user_id == FoodUserRecommendation.user_id
    ).distinct(FoodRecommendation.id)
    return recommendations


def get_today_recommendation(user_id):
    recommendation = FoodRecommendation.query.join(FoodUserRecommendation).filter(
            user_id == FoodUserRecommendation.user_id
    ).order_by(FoodUserRecommendation.created_at.desc()).first()
    return recommendation


def get_last_score(user_id, frequency_id):
    score = 0
    solved_questionnaires = SolvedQuestionnaire.query.filter(
        user_id == SolvedQuestionnaire.user_id,
        SolvedQuestionnaire.score != 0
    ).join(Questionnaire).filter(
        frequency_id == Questionnaire.frequency_id
    ).all()
    for solved in solved_questionnaires:
        today = solved.created_at.strftime("%Y-%m-%d")
        if today == get_date():
            score = solved.score
    return score


def get_recommendation_user(user_id, frequency_id):
    existed = None
    recommendations_user = FoodUserRecommendation.query.filter(
        FoodUserRecommendation.user_id == user_id 
    ).join(FoodRecommendation).filter(
        FoodRecommendation.frequency_id == frequency_id
    ).all()
    for recommendation_user in recommendations_user:
        today = recommendation_user.created_at.strftime("%Y-%m-%d")
        if today == get_date():
            existed = recommendation_user

    return existed 


def get_recommendation_frequency(frequency_id, score):
    recommendation = FoodRecommendation.query.filter(
            frequency_id == FoodRecommendation.frequency_id,
            score >= FoodRecommendation.min,
            score <= FoodRecommendation.max
    ).first()
    return recommendation


def add_recommendation_to_user(user_id, frequency_id, score):

    existed = get_recommendation_user(user_id, frequency_id)

    if existed:
        last_score = get_last_score(user_id, frequency_id)
        recommendation = get_recommendation_frequency(frequency_id, score)
        existed.food_recommendation_id = recommendation.id
        existed.update() 
    else:
        recommendation = get_recommendation_frequency(frequency_id, score)
        created = FoodUserRecommendation(user_id, recommendation.id)
        created.save()
        created.commit()
