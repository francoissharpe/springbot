from flask_restful import Resource
from springbot.api.teams.models import Team
from springbot.api.teams.schemas import team_schema, teams_schema


class TeamCollection(Resource):
    def get(self):
        teams = Team.query.all()
        return teams_schema.dump(teams)


class TeamItem(Resource):
    def get(self, team_id):
        team = Team.query.get(team_id)
        return team_schema.dump(team)
