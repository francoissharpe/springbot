from flask import Blueprint
from flask_restful import Api
from springbot.api.teams.endpoints import TeamCollection, TeamItem
from springbot.api.players.endpoints import PlayerCollection, PlayerItem


api = Api()
bp = Blueprint('api', __name__)
api.init_app(bp)

api.add_resource(TeamCollection, '/teams/')
api.add_resource(TeamItem, '/teams/<int:team_id>')
api.add_resource(PlayerCollection, '/players/')
api.add_resource(PlayerItem, '/players/<int:player_id>')
