from flask_restful import Resource
from springbot.models.teams import Team


class TeamCollection(Resource):
    def get(self):
        return [result.serialize() for result in Team.query.all()]


class TeamItem(Resource):
    def get(self, team_id):
        return Team.query.get(team_id).serialize()
