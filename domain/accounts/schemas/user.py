from extensions.database_extension import ma
from marshmallow import post_dump
from domain.accounts.models.user import User
from domain.commons.util import format_date_to_show

class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "first_name", "last_name", "email", "genre", "birth_date")
        model = User
    
    @post_dump()
    def get_data(self, data, **kwargs):
        birth_date = data['birth_date']
        data['birth_date'] = format_date_to_show(birth_date)
        return data
