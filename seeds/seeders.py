from flask_seeder import Seeder
from domain.motivations.models.frequency import Frequency
from domain.motivations.models.motivation_type import MotivationType
from domain.motivations.models.phrase import Phrase

class FrequencySeeder(Seeder):
    def run(self):
        values = ['Anual', 'Mensual', 'Quincenal', 'Semanal']
        for index, value in enumerate(values):
            exists = Frequency.get_one(**{'name': value})
            if not exists:
                frequency = Frequency(value)
                self.db.session.add(frequency)


class MotivationTypeSeeder(Seeder):
    def run(self):
        values = ['Fisica', 'Alimenticia']
        for index, value in enumerate(values):
            exists = MotivationType.get_one(**{'name': value})
            if not exists:
                motivation_type = MotivationType(value)
                self.db.session.add(motivation_type)


class PhraseSeeder(Seeder):
    def run(self):
        values = [
            {'title': 'Tu puedes aumentar tu fisico', 'icon': 'happy', 'type_id': 1}, 
            {'title': 'Estas siguiendo la dieta!!!', 'icon': 'sad', 'type_id': 2}, 
            {'title': 'Bien hecho!! sigue con esas flexiones', 'icon': 'angry', 'type_id': 1}, 
        ]
        for index, value in enumerate(values):
            title = value.get('title')
            icon = value.get('icon')
            type_id = value.get('type_id')
            exists = Phrase.get_one(**{'title': title})
            if not exists:
                phrase = Phrase(title, icon, type_id)
                self.db.session.add(phrase)
