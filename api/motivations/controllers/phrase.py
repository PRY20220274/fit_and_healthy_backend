from flask import request
from flask_restx import Resource
from api.motivations.adapters.docs.phrase import phrase_namespace
from api.motivations.adapters.responses.phrase import phrase_response
from domain.motivations.schemas.phrase import PhraseSchema
from domain.motivations.services.phrase import get_random_phrase
from domain.commons.util import get_param

@phrase_namespace.route('/random')
@phrase_namespace.doc(params={'type': 'Motivation Type Id'})
class PhraseDetailResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.schema = PhraseSchema()

    @phrase_namespace.response(code=200, description='Success', model=phrase_response)
    @phrase_namespace.response(code=400, description='Bad Request')
    def get(self):
        params = request.args
        type = get_param(params, 'type')
        phrase = get_random_phrase(type)
        response = self.schema.dump(phrase)
        return response, 200
