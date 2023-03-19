from api.fit.adapters.docs.iot import iot_namespace
from flask_restx import fields


access_request = iot_namespace.model('AccessRequest', {
    'code': fields.String,
})
