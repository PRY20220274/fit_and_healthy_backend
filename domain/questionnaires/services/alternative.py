from domain.questionnaires.models.alternative import Alternative
from extensions.exception_extension import NotFoundException


def get_alternative(id):
    alternative = Alternative.get_by_id(id)
    if alternative:
        return alternative
    else:
        raise NotFoundException('alternative', 'id', id)
