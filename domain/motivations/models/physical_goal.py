from extensions.database_extension import db
from domain.motivations.models.goal import Goal
from domain.commons.util import get_datetime, format_date_to_save

class PhysicalGoal(Goal):
    __tablename__ = 'physical_goals'

    id = db.Column(db.Integer, db.ForeignKey('goals.id'), primary_key=True)
    steps = db.Column(db.Integer, nullable=False)
    kilometers = db.Column(db.Integer, nullable=False)
    cardio_points = db.Column(db.Integer, nullable=False)
    calories = db.Column(db.Integer, nullable=False)
    frequency_id = db.Column(db.Integer, db.ForeignKey('frequencies.id'))
    frequency = db.relationship("Frequency")

    __mapper_args__ = {
        'polymorphic_identity': 'physical_goal',
    }

    def __init__(self, steps, kilometers, cardio_points, calories):
        self.type = 'physical_goal'
        self.steps = steps
        self.kilometers = kilometers
        self.cardio_points = cardio_points
        self.calories = calories
        self.created_at = get_datetime()
