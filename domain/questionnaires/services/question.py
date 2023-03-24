from domain.questionnaires.models.question import Question
from extensions.exception_extension import NotFoundException


def get_question(id):
    question = Question.get_by_id(id)
    if question:
        return question
    else:
        raise NotFoundException('question', 'id', id)
