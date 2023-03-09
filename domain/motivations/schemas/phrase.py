from extensions.database_extension import ma
from extensions.exception_extension import BadRequestException
from domain.motivations.models.phrase import Phrase


class PhraseSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "icon", "type")
        model = Phrase

    type = ma.Method("get_type")

    def get_type(self, obj):
        type = obj.type
        return type.name
