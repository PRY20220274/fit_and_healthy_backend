from domain.questionnaires.models.solved_questionnaire import SolvedQuestionnaire
from domain.questionnaires.services.questionnaire import get_questionnaire
from extensions.exception_extension import NotFoundException

def build_questionnaire(data):
    questionnaire_id = data.get('questionnaire', None)
    return questionnaire_id

def save_solved(user_id, questionnaire_id):

    solved = SolvedQuestionnaire()
    solved.user_id = user_id

    if questionnaire_id is not None:
        if get_questionnaire(questionnaire_id):
            solved.questionnaire_id = questionnaire_id
    
    solved.score = 0
    created = solved.save()
    created.commit()
    return created
