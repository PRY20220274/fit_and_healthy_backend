from extensions.database_extension import db
from domain.motivations.models.goal import Goal
from domain.commons.util import get_datetime

class FoodGoal(Goal):
    __tablename__ = 'food_goals'

    id = db.Column(db.Integer, db.ForeignKey('goals.id'), primary_key=True)
    objective_id = db.Column(db.Integer, db.ForeignKey('objectives.id'))
    objective = db.relationship("Objective")
    activity_id = db.Column(db.Integer, db.ForeignKey('activities.id'))
    activity = db.relationship("Activity")

    __mapper_args__ = {
        'polymorphic_identity': 'food_goal',
    }

    def __init__(self, description, type):
        self.description = description
        self.type = 'food_goal'
        self.created_at = get_datetime()
