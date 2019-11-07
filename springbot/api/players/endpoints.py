from flask_restful import Resource
from springbot.api.players.models import Player
from springbot.api.players.schemas import player_schema, players_schema


class PlayerCollection(Resource):
    def get(self):
        players = Player.query.all()
        return players_schema.dump(players)


class PlayerItem(Resource):
    def get(self, player_id):
        player = Player.query.get(player_id)
        return player_schema.dump(player)
