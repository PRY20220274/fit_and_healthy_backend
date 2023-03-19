from extensions.database_extension import db, BaseModel

class Access(db.Model, BaseModel):
    __tablename__ = 'access'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    access_token = db.Column(db.Text, nullable=False)
    refresh_token = db.Column(db.Text, nullable=False)
    scope = db.Column(db.Text, nullable=False)
    token_type = db.Column(db.String(7), nullable=False)
    expiry_date = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User")

    def __init__(self, access_token, refresh_token, scope, token_type, expiry_date):
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.scope = scope
        self.token_type = token_type
        self.expiry_date = expiry_date

    def to_dict(self):
        return {
            'access_token': self.access_token,
            'refresh_token': self.refresh_token,
            'scope': self.scope,
            'token_type': self.token_type,
            'expiry_date': self.expiry_date
        }