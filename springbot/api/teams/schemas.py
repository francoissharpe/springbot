from springbot import ma
from springbot.api.teams.models import Team


class TeamSchema(ma.ModelSchema):
    class Meta:
        model = Team


team_schema = TeamSchema()
teams_schema = TeamSchema(many=True)
