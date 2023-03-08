from extensions.database_extension import ma
from domain.motivations.models.motivation_type import MotivationType
from domain.commons.util import format_date_to_show

class MotivationTypeSchema(ma.Schema):
    class Meta:
        fields = ("id", "name")
        model = MotivationType
