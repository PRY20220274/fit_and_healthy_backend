from domain.motivations.models.phrase import Phrase
from domain.motivations.models.motivation_type import MotivationType
from sqlalchemy.sql.expression import func

def get_random_phrase(type):
    phrase = Phrase.query.join(MotivationType).filter_by(name=type).order_by(func.random()).first()
    return phrase
