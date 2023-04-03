from marshmallow import post_load
from extensions.database_extension import ma
from domain.motivations.models.food_goal import FoodGoal


class FoodGoalSchema(ma.Schema):
    class Meta:
        fields = ("id", "description", "activity", 'objective', 'completed')
        model = FoodGoal

    activity = ma.Method("get_activity")
    objective = ma.Method("get_objective")
    completed = ma.Method("get_completed")

    def get_activity(self, obj):
        activity = obj.activity 
        return activity.name

    def get_objective(self, obj):
        objective = obj.objective 
        return objective.name

    def get_completed(self, obj):
        completed = obj.completed
        if completed == False:
            return "No completado"
        else:
            return "Completado"

    @post_load
    def make_goal(self, data, **kwargs):
        return FoodGoal(**data)