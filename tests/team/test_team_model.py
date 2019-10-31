from springbot.models.teams import Team


def test_initial_team_created_from_collection(init_db):
    teams = Team.query.all()
    assert len(teams) == 1
    assert teams[0].name == 'South Africa'
    assert teams[0].id == 1


def test_initial_team_created_from_id(init_db):
    teams = Team.query.get(1)
    assert teams.name == 'South Africa'
    assert teams.id == 1


