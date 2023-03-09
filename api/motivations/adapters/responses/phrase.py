from api.motivations.adapters.docs.phrase import phrase_namespace
from flask_restx import fields


phrase_response = phrase_namespace.model('PhraseResponse', {
    'id': fields.Integer,
    'title': fields.String,
    'icon': fields.String,
    'type': fields.String
})
