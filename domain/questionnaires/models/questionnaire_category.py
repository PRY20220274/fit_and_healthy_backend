from extensions.database_extension import db, BaseModel

class QuestionnaireCategory(db.Model, BaseModel):
    __tablename__ = 'questionnaire_categories'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    icon = db.Column(db.String(15), nullable=False)

    def __init__(self, name, description, icon):
        self.name = name
        self.description = description
        self.icon = icon
