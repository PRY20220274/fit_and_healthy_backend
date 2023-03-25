from domain.questionnaires.models.solved_questionnaire import SolvedQuestionnaire
from domain.questionnaires.models.solved_questionnaire_detail import SolvedQuestionnaireDetail
from domain.questionnaires.services.questionnaire import get_questionnaire
from domain.questionnaires.services.question import get_question
from domain.questionnaires.services.alternative import get_alternative
from extensions.exception_extension import BadRequestException


def build_answers(answer_ids):
    answers = []
    for alternative_id in answer_ids:
        alternative = get_alternative(alternative_id)
        question = get_question(alternative.question_id)
        answers.append({'alternative': alternative, 'question': question})
    return answers


def build_questionnaire(data):
    questionnaire_id = data.get('questionnaire', None)
    answer_ids = data.get('answers', [])
    questionnaire = None
    answers = []
    errors = {}

    if questionnaire_id is not None:
        questionnaire = get_questionnaire(questionnaire_id)
    else:
        errors['questionnaire'] = 'Questionnaire is required'
    
    if len(answer_ids) != 0:
        answers = build_answers(answer_ids)
    else:
        errors['answers'] = 'Answers are required'

    if errors:
        raise BadRequestException(errors)

    return questionnaire, answers


def save_solved(user_id, questionnaire_id, answers):
    solved = SolvedQuestionnaire()
    solved.user_id = user_id
    solved.questionnaire_id = questionnaire_id
    
    if questionnaire_id is not None:
        if get_questionnaire(questionnaire_id):
            solved.questionnaire_id = questionnaire_id

    score = 0
    solved.score = score
    created = solved.save()
    created.commit()
    
    for answer in answers:
        question = answer.get('question')
        alternative = answer.get('alternative')

        score = score + alternative.score
        detail = SolvedQuestionnaireDetail(created.id, question.id, alternative.id)
        detail.save()
        detail.commit()
    
    created.score = score
    updated = created.update()
    return updated
