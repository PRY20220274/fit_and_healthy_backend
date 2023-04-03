from extensions.database_extension import ma
from domain.motivations.models.frequency import Frequency

class FrequencySchema(ma.Schema):
    class Meta:
        fields = ("id", "name")
        model = Frequency
