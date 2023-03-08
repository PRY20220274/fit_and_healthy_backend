from api.motivations.adapters.docs.phrase import phrase_namespace
from api.motivations.adapters.responses.motivation_type import motivation_type_response
from flask_restx import fields


phrase_response = phrase_namespace.model('PhraseResponse', {
    'id': fields.Integer,
    'title': fields.String,
    'icon': fields.String,
    'type': fields.Nested(motivation_type_response)
})
