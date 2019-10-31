from flask_restful import Api
from springbot.resources.teams.team import TeamCollection, TeamItem


api = Api()
api.add_resource(TeamCollection, '/teams/')
api.add_resource(TeamItem, '/teams/<int:team_id>')
