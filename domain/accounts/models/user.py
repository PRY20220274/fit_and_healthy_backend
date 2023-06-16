from extensions.database_extension import db, BaseModel
from domain.commons.util import get_datetime, format_date_to_save, is_date

class User(db.Model, BaseModel):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    genre = db.Column(db.String(1), nullable=False)
    birth_date = db.Column(db.Date, nullable=True)
    weights = db.relationship('Weight', backref='user', lazy=True)
    height = db.Column(db.Float)
    state = db.Column(db.Boolean, nullable=False, default=True)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, first_name, last_name,  email, password, genre, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.genre = genre
        self.birth_date = format_date_to_save(birth_date)
        self.created_at = get_datetime()

    def format_date(self):
        valid = is_date(self.birth_date)
        if not is_date(self.birth_date):
            self.birth_date = format_date_to_save(self.birth_date)
