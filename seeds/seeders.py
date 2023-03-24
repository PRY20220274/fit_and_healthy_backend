from flask_seeder import Seeder
from domain.motivations.models.frequency import Frequency
from domain.motivations.models.motivation_type import MotivationType
from domain.motivations.models.phrase import Phrase
from domain.questionnaires.models.questionnaire_category import QuestionnaireCategory
from domain.questionnaires.models.questionnaire import Questionnaire

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


class QuestionnaireCategorySeeder(Seeder):
    def run(self):
        values = [
            {'name': 'Alimentos comestibles', 'description': 'Esta es la categoria para los cuestionarios de alimentos comestibles', 'icon': 'comestible'}, 
            {'name': 'Liquidos', 'description': 'Esta es la categoria para los cuestionarios liquidos', 'icon': 'liquido'}
        ]
        for index, value in enumerate(values):
            name = value.get('name')
            description = value.get('description')
            icon = value.get('icon')
            exists = QuestionnaireCategory.get_one(**{'name': name})
            if not exists:
                category = QuestionnaireCategory(name, description, icon)
                self.db.session.add(category)


class QuestionnaireSeeder(Seeder):
    def run(self):
        values = [
            {
                'name': 'Cuestionario de alimentos comestibles desayuno', 
                'start_hour': '00:00:00', 
                'end_hour': '11:00:00',
                'category_id': 1
            },
            {
                'name': 'Cuestionario de alimentos comestibles almuerzo', 
                'start_hour': '11:00:00', 
                'end_hour': '18:00:00',
                'category_id': 1
            },
            {
                'name': 'Cuestionario de alimentos comestibles cena', 
                'start_hour': '18:00:00', 
                'end_hour': '24:00:00',
                'category_id': 1
            },
            {
                'name': 'Cuestionario de liquidos desayuno', 
                'start_hour': '00:00:00', 
                'end_hour': '11:00:00',
                'category_id': 2
            },
            {
                'name': 'Cuestionario de liquidos almuerzo', 
                'start_hour': '11:00:00', 
                'end_hour': '18:00:00',
                'category_id': 2
            },
            {
                'name': 'Cuestionario de liquidos cena', 
                'start_hour': '18:00:00', 
                'end_hour': '24:00:00',
                'category_id': 2
            },
        ]
        for index, value in enumerate(values):
            name = value.get('name')
            start_hour = value.get('start_hour')
            end_hour = value.get('end_hour')
            category_id = value.get('category_id')
            exists = Questionnaire.get_one(**{'name': name})
            if not exists:
                questionnaire = Questionnaire(name, start_hour, end_hour, category_id)
                self.db.session.add(questionnaire)
