from extensions.database_extension import ma
from domain.recommendations.models.food_recommendation import FoodRecommendation
from domain.recommendations.models.frequency_food import FrequencyFood

class FoodRecommendationSchema(ma.Schema):
    class Meta:
        fields = ("id", "description")
        model = FoodRecommendation
