import pytest
from springbot import create_app, db
from springbot.api.teams.models import Team
from springbot.api.players.models import Player


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('test-springbot.cfg')
    testing_client = flask_app.test_client()
    ctx = flask_app.app_context()
    ctx.push()
    yield testing_client
    ctx.pop()


@pytest.fixture(scope='module')
def init_db(test_client):
    db.create_all()
    team = Team(name='South Africa')
    player = Player(name='Francois')
    db.session.add(team)
    db.session.add(player)
    db.session.commit()
    yield db
    db.drop_all()


@pytest.fixture(scope='module')
def test_client_with_db(test_client):
    db.create_all()
    team = Team(name='South Africa')
    player = Player(name='Francois')
    db.session.add(team)
    db.session.add(player)
    db.session.commit()
    yield test_client
    db.drop_all()
