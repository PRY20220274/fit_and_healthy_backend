from domain.motivations.models.frequency import Frequency

def get_frequencies():
    frequencies = Frequency.get_all()
    return frequencies

def get_frequency(id):
    frequency = Frequency.get_by_id(id)
    if frequency:
        return frequency
    else:
        raise NotFoundException('frequency', 'id', id)
