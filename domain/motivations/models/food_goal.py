from extensions.database_extension import db, BaseModel
from domain.commons.util import get_datetime

class FoodGoal(db.Model, BaseModel):
    __tablename__ = 'food_goals'

    id = db.Column(db.Integer, db.ForeignKey('goals.id'), primary_key=True)
    objective_id = db.Column(db.Integer, db.ForeignKey('objectives.id'))
    objective = db.relationship("Objective")
    activity_id = db.Column(db.Integer, db.ForeignKey('activities.id'))
    activity = db.relationship("Activity")

    __mapper_args__ = {
        'polymorphic_identity': 'food_goal',
    }

    def __init__(self, description):
        self.description = description
        self.created_at = get_datetime()
