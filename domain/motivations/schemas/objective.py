from extensions.database_extension import ma
from domain.motivations.models.objective import Objective

class ObjectiveSchema(ma.Schema):
    class Meta:
        fields = ("id", "name")
        model = Objective
