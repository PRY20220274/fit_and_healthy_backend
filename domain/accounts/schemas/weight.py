from extensions.database_extension import ma
from marshmallow import post_dump
from domain.accounts.models.weight import Weight
from domain.commons.util import format_date_to_show

class WeightSchema(ma.Schema):
    class Meta:
        fields = ("id", "value", "created_at")
        model = Weight
