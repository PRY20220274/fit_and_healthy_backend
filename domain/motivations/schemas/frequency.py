from extensions.database_extension import ma
from domain.motivations.models.frequency import Frequency
from domain.commons.util import format_date_to_show

class FrequencySchema(ma.Schema):
    class Meta:
        fields = ("id", "name")
        model = Frequency
