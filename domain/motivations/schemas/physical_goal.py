from marshmallow import post_load
from extensions.database_extension import ma
from domain.motivations.models.physical_goal import PhysicalGoal


class PhysicalGoalSchema(ma.Schema):
    class Meta:
        fields = ("id", "description", "steps", "kilometers", "cardio_points", "calories", "frequency", 'completed')
        model = PhysicalGoal

    frequency = ma.Method("get_frequency")
    completed = ma.Method("get_completed")

    def get_frequency(self, obj):
        frequency = obj.frequency 
        return frequency.name

    def get_completed(self, obj):
        completed = obj.completed
        if completed == False:
            return "No completado"
        else:
            return "Completado"

    @post_load
    def make_goal(self, data, **kwargs):
        return PhysicalGoal(**data)