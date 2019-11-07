from springbot.api.players.models import Player


def test_initial_player_created_from_collection(init_db):
    players = Player.query.all()
    assert len(players) == 1
    assert players[0].name == 'Francois'
    assert players[0].id == 1


def test_initial_player_created_from_id(init_db):
    player = Player.query.get(1)
    assert player.name == 'Francois'
    assert player.id == 1


