from extensions.database_extension import ma
from marshmallow import post_dump
from domain.fit.models.physical_data import PhysicalData
from domain.commons.util import format_datetime_to_show

class PhysicalDataSchema(ma.Schema):
    class Meta:
        fields = ("id", "steps", "calories", "cardio_points", "heart_rate", "breathing_rate", 
                  "kilometers_traveled", "width", "height", "created_at")
        model = PhysicalData
    
    @post_dump()
    def get_data(self, data, **kwargs):
        created_at = data['created_at']
        data['created_at'] = format_datetime_to_show(created_at)
        return data
