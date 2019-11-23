from flask import request
from flask_restful import Resource
from springbot import db
from springbot.api.teams.models import Team
from springbot.api.teams.schemas import team_schema, teams_schema


def entry_already_exists(name):
    return Team.query.filter_by(name=name).first()


class TeamCollection(Resource):
    def get(self):
        teams = Team.query.all()
        return teams_schema.dump(teams), 200

    def post(self):
        data = team_schema.load(request.get_json())
        if entry_already_exists(data['name']):
            return {'message': f'Entry [{data.get("name")}] already exists.'}, 419
        new_team = Team(name=data["name"])
        db.session.add(new_team)
        db.session.commit()
        return team_schema.dump(new_team), 201


class TeamItem(Resource):
    def get(self, team_id):
        team = Team.query.get(team_id)
        return team_schema.dump(team), 200
