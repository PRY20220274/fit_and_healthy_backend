from api.auth.routes import auth_blueprint
from api.accounts.routes import accounts_blueprint
from api.motivations.routes import motivations_blueprint
from api.recommendations.routes import recommendations_blueprint
from api.questionnaires.routes import questionnaires_blueprint
from api.fit.routes import fit_blueprint

def register_routes(app):
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(accounts_blueprint)
    app.register_blueprint(motivations_blueprint)
    app.register_blueprint(recommendations_blueprint)
    app.register_blueprint(questionnaires_blueprint)
    app.register_blueprint(fit_blueprint)