from marshmallow import post_load, validates_schema
from extensions.database_extension import ma
from extensions.exception_extension import BadRequestException
from domain.accounts.schemas.user import UserSchema
from domain.motivations.models.goal import Goal


class GoalSchema(ma.Schema):
    class Meta:
        fields = ("id", "description", "user")
        model = Goal

    user = ma.Nested(UserSchema)
    
    @validates_schema()
    def validate_user(self, data, **kwargs):
        errors = {}
        description = data.get('description', None)
        if description is None:
            errors['description'] = 'Description is required'
        if description == '':
            errors['description'] = 'Description must not be blank'
        if errors:
            raise BadRequestException(errors)

    @post_load
    def make_goal(self, data, **kwargs):
        return Goal(**data)