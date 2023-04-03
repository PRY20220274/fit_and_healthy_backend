from flask_seeder import Seeder
from domain.questionnaires.models.questionnaire_category import QuestionnaireCategory
from domain.recommendations.models.frequency_food import FrequencyFood
from domain.questionnaires.models.questionnaire import Questionnaire
from domain.questionnaires.models.question import Question
from domain.questionnaires.models.alternative import Alternative
from domain.questionnaires.models.scale import Scale
from domain.recommendations.models.food_recommendation import FoodRecommendation
from domain.recommendations.models.physical_recommendation import PhysicalRecommendation
from domain.motivations.models.frequency import Frequency
from domain.motivations.models.activity import Activity
from domain.motivations.models.objective import Objective


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


class FrequencyFoodSeeder(Seeder):
    def run(self):
        values = [
            {
                'name': 'Desayuno',
                'start_hour': '00:00:00', 
                'end_hour': '11:00:00'
            },
            {
                'name': 'Almuerzo',
                'start_hour': '11:00:00', 
                'end_hour': '18:00:00'
            },
            {
                'name': 'Cena',
                'start_hour': '18:00:00', 
                'end_hour': '24:00:00'
            }
        ]
        for index, value in enumerate(values):
            name = value.get('name')
            exists = FrequencyFood.get_one(**{'name': name})
            if not exists:
                frequency_food = FrequencyFood(name)
                self.db.session.add(frequency_food)


class QuestionnaireSeeder(Seeder):
    def run(self):
        values = [
            {
                'name': 'Cuestionario de alimentos comestibles desayuno', 
                'category_id': 1,
                'frequency_id': 1,
            },
            {
                'name': 'Cuestionario de alimentos comestibles almuerzo', 
                'category_id': 1,
                'frequency_id': 2
            },
            {
                'name': 'Cuestionario de alimentos comestibles cena', 
                'category_id': 1,
                'frequency_id': 3
            },
            {
                'name': 'Cuestionario de liquidos desayuno', 
                'category_id': 2,
                'frequency_id': 1,
            },
            {
                'name': 'Cuestionario de liquidos almuerzo', 
                'category_id': 2,
                'frequency_id': 2
            },
            {
                'name': 'Cuestionario de liquidos cena', 
                'category_id': 2,
                'frequency_id': 3
            },
        ]
        for index, value in enumerate(values):
            name = value.get('name')
            category_id = value.get('category_id')
            frequency_id = value.get('frequency_id')
            exists = Questionnaire.get_one(**{'name': name})
            if not exists:
                questionnaire = Questionnaire(name, frequency_id, category_id)
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


class FoodRecommendationSeeder(Seeder):
    def run(self):
        values = [
            {
                'description': 'La cantidad de calorías consumidas no son suficientes para tu cuerpo. Puedes hacer un batido de fresas con leche y un plátano y  aporta 350 calorías. Un sándwich con pollo, lechuga y tomate aporta 300 calorías.',
                'min': 0,
                'max': 3,
                'frequency_id': 1
            },
            {
                'description': 'Un omelet de espinacas con un pan integral y zumo de naranja es una buena opción,ya que tiene un aporte calórico de 350. Otra buena opción es la leche desnatada con avena, fruta y semillas de chía, nos aporta 380 calorías.',
                'min': 4,
                'max': 6,
                'frequency_id': 1
            },
            {
                'description': 'Estás muy cerca de tener un desayuno balanceado, te falta poco, puedes aumentar unas cuantas calorías con una ensalada de frutas que aporta 200 calorías.',
                'min': 7,
                'max': 9,
                'frequency_id': 1
            },
            {
                'description': 'Los frutos secos, los cereales y los panes integrales contienen fibra, si combinamos ¼ de taza con un vaso de yogurt y unas almendras picadas, nos aseguran 160 calorías. Un jugo de manzana sin azúcar nos da 150 calorías.',
                'min': 10,
                'max': 12,
                'frequency_id': 1
            },
            {
                'description': 'Puedes reducir el consumo de calorías, puedes hacer un yogurt griego con kiwi y arándanos, nos aporta 130 calorías. También tenemos la opción de una tostada con palta y queso, que nos da 150 calorías.',
                'min': 13,
                'max': 15,
                'frequency_id': 1
            },
            {
                'description': 'Una crema de trigo, es una gran opción para el desayuno, nos da 110 Calorías. Podemos  hacer una rebanada mediana de tostada francesa con miel, que nos da 200 calorías.',
                'min': 16,
                'max': 18,
                'frequency_id': 1
            }
        ]
        for index, value in enumerate(values):
            description = value.get('description')
            min = value.get('min')
            max = value.get('max')
            frequency_id = value.get('frequency_id')
            exists = FoodRecommendation.get_one(**{'description': description})
            if not exists:
                recommendation = FoodRecommendation(description, min, max, frequency_id)
                self.db.session.add(recommendation)


class FrequencySeeder(Seeder):
    def run(self):
        values = ['Anual', 'Mensual', 'Quincenal', 'Semanal']
        for index, value in enumerate(values):
            exists = Frequency.get_one(**{'name': value})
            if not exists:
                frequency = Frequency(value)
                self.db.session.add(frequency)


class ObjectiveSeeder(Seeder):
    def run(self):
        values = ['Engordar', 'Adelgazar', 'Mantener']
        for index, value in enumerate(values):
            exists = Objective.get_one(**{'name': value})
            if not exists:
                objective = Objective(value)
                self.db.session.add(objective)

