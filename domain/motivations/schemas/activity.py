from extensions.database_extension import ma
from domain.motivations.models.activity import Activity

class ActivitySchema(ma.Schema):
    class Meta:
        fields = ("id", "name")
        model = Activity
