from extensions.database_extension import db, BaseModel
from domain.commons.util import get_datetime

class PhysicalData(db.Model, BaseModel):
    __tablename__ = 'physical_data'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    steps = db.Column(db.Integer)
    calories = db.Column(db.Integer)
    cardio_points = db.Column(db.Integer)
    heart_rate = db.Column(db.Integer)
    breathing_rate = db.Column(db.Integer)
    kilometers_traveled = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User")

    def __init__(self, steps, calories, cardio_points, heart_rate, breathing_rate, kilometers_traveled):
        self.steps = steps
        self.calories = calories
        self.cardio_points = cardio_points
        self.heart_rate = heart_rate
        self.breathing_rate = breathing_rate
        self.kilometers_traveled = kilometers_traveled
        self.created_at = get_datetime()
