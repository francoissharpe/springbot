from springbot import db


class Player(db.Model):
    __tablename__ = 'players'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    full_name = db.Column(db.String(160), nullable=True)
    birthday = db.Column(db.DateTime, nullable=True)
    height = db.Column(db.Float, nullable=True)
    weight = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return f"<Player id='{self.id} name='{self.name}'>"
