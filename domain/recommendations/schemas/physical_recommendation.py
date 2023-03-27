from extensions.database_extension import ma
from domain.recommendations.models.physical_recommendation import PhysicalRecommendation

class PhysicalRecommendationSchema(ma.Schema):
    class Meta:
        fields = ("id", "description")
        model = PhysicalRecommendation
