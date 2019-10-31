import json


def test_get_all(test_client_with_db):
    response = test_client_with_db.get('/teams/')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert len(data) == 1
    assert data[0].get('id') == 1


def test_team_by_id(test_client_with_db):
    response = test_client_with_db.get('/teams/1')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data.get('id') == 1
