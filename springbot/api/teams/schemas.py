from marshmallow import fields
from springbot import ma


class TeamSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)


team_schema = TeamSchema()
teams_schema = TeamSchema(many=True)
