from extensions.database_extension import ma
from domain.questionnaires.models.alternative import Alternative

class AlternativeSchema(ma.Schema):
    class Meta:
        fields = ("id", "description", "score")
        model = Alternative
