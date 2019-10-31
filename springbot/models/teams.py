from springbot import db


class Team(db.Model):
    __tablename__ = 'team'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Team id='{self.id} name='{self.name}''>"

    def serialize(self):
        return {'id': self.id, 'name': self.name}
