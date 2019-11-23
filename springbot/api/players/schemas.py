from marshmallow import fields
from springbot import ma


class PlayerSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    full_name = fields.String(required=False)
    birthday = fields.DateTime(required=False)
    height = fields.Float(required=False)
    weight = fields.Float(required=False)


player_schema = PlayerSchema()
players_schema = PlayerSchema(many=True)
