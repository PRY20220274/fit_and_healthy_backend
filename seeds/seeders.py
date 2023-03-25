from flask_seeder import Seeder
from domain.motivations.models.frequency import Frequency
from domain.motivations.models.motivation_type import MotivationType
from domain.motivations.models.phrase import Phrase
from domain.questionnaires.models.questionnaire_category import QuestionnaireCategory
from domain.questionnaires.models.questionnaire import Questionnaire
from domain.questionnaires.models.question import Question
from domain.questionnaires.models.alternative import Alternative
from domain.questionnaires.models.scale import Scale

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


class QuestionSeeder(Seeder):
    def run(self):
        values = [
            {
                'description': 'En el desayuno comiste…', 
            },
            {
                'description': '¿Qué tipo de cereales consumiste?', 
            },
            {
                'description': 'Las proteínas son muy importantes, cuéntanos cuales comiste hoy…', 
            },
            {
                'description': '¿Pudiste comer grasas saludables?', 
            },
        ]
        for index, value in enumerate(values):
            description = value.get('description')
            exists = Question.get_one(**{'description': description})
            if not exists:
                question = Question(description)
                self.db.session.add(question)


class AlternativeSeeder(Seeder):
    def run(self):
        values = [
            {
                'description': 'Frutas(ensalada o fruta sola)',
                'score': 2,
                'question_id': 1
            },
            {
                'description': 'Verduras(ensalada fresca o cocida)',
                'score': 1,
                'question_id': 1
            },
            {
                'description': 'Ninguna',
                'score': 0,
                'question_id': 1
            },
            {
                'description': 'Arroz',
                'score': 1,
                'question_id': 2
            },
            {
                'description': 'Avena',
                'score': 4,
                'question_id': 2
            },
            {
                'description': 'Trigo',
                'score': 2,
                'question_id': 2
            },
            {
                'description': 'Quinoa',
                'score': 5,
                'question_id': 2
            },
            {
                'description': 'Kiwicha',
                'score': 6,
                'question_id': 2
            },
            {
                'description': 'Cañihua',
                'score': 3,
                'question_id': 2
            },
            {
                'description': 'Ninguno',
                'score': 0,
                'question_id': 2
            },
            {
                'description': 'Huevo cocido',
                'score': 2,
                'question_id': 3
            },
            {
                'description': 'Huevo frito',
                'score': 1,
                'question_id': 3
            },
            {
                'description': 'Yogurt',
                'score': 3,
                'question_id': 3
            },
            {
                'description': 'Queso',
                'score': 4,
                'question_id': 3
            },
            {
                'description': 'Ninguno',
                'score': 0,
                'question_id': 3
            },
            {
                'description': 'Almendras',
                'score': 3,
                'question_id': 4
            },
            {
                'description': 'Nueces',
                'score': 4,
                'question_id': 4
            },
            {
                'description': 'Pistacho',
                'score': 2,
                'question_id': 4
            },
            {
                'description': 'Castañas',
                'score': 1,
                'question_id': 4
            },
            {
                'description': 'Ninguno',
                'score': 0,
                'question_id': 4
            },
        ]
        for index, value in enumerate(values):
            description = value.get('description')
            score = value.get('score')
            question_id = value.get('question_id')
            exists = Alternative.get_one(**{'description': description})
            if not exists:
                alternative = Alternative(description, score, question_id)
                self.db.session.add(alternative)


class AlternativeSeeder(Seeder):
    def run(self):
        values = [
            {
                'description': 'Deberías aumentar el consumo de calorías.',
                'min': 0,
                'max': 16,
                'questionnaire_id': 7
            },
            {
                'description': 'Tu consumo es balanceado, sigue asi.',
                'min': 17,
                'max': 32,
                'questionnaire_id': 7
            },
            {
                'description': 'Parece que estás consumiendo calorías extras y empieza a balancear tu comida. Un buen desayuno consta de:',
                'min': 33,
                'max': 48,
                'questionnaire_id': 7
            },
        ]
        for index, value in enumerate(values):
            description = value.get('description')
            min = value.get('min')
            max = value.get('max')
            questionnaire_id = value.get('questionnaire_id')
            exists = Scale.get_one(**{'description': description})
            if not exists:
                scale = Scale(description, min, max, questionnaire_id)
                self.db.session.add(scale)
