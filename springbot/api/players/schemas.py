from springbot import ma
from springbot.api.players.models import Player


class PlayerSchema(ma.ModelSchema):
    class Meta:
        model = Player


player_schema = PlayerSchema()
players_schema = PlayerSchema(many=True)
