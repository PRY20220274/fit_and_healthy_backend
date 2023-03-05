from api.auth.routes import auth_blueprint
from api.accounts.routes import accounts_blueprint

def register_routes(app):
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(accounts_blueprint)
    #app.register_blueprint(medical_risks_blueprint)
    #app.register_blueprint(medical_monitoring_blueprint)
