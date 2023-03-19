from api.fit.adapters.docs.iot import iot_namespace
from flask_restx import fields


url_response = iot_namespace.model('UrlResponse', {
    'url': fields.String,
})


access_response = iot_namespace.model('AccessResponse', {
    'message': fields.String,
})

iot_response = iot_namespace.model('IotResponse', {
    'message': fields.String,
})
