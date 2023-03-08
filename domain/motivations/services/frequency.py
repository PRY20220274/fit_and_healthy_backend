from domain.motivations.models.frequency import Frequency

def get_frequencies():
    frequencies = Frequency.get_all()
    return frequencies
