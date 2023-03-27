from extensions.database_extension import db, BaseModel
from sqlalchemy.dialects.mysql import TIME

class FrequencyFood(db.Model, BaseModel):
    __tablename__ = 'frequency_food'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    start_hour = db.Column(TIME(), nullable=False)
    end_hour = db.Column(TIME(), nullable=False)

    def __init__(self, name, start_hour, end_hour):
        self.name = name
        self.start_hour = start_hour
        self.end_hour = end_hour
