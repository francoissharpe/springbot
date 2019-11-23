import os
import json


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def get_by_id(test_client_with_db, _id):
    response = test_client_with_db.get(f'/teams/{_id}')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data.get('id') == _id


def test_get_all(test_client_with_db):
    response = test_client_with_db.get('/teams/')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert len(data) == 1
    assert data[0].get('id') == 1


def test_get_by_id(test_client_with_db):
    get_by_id(test_client_with_db, 1)


def test_create(test_client_with_db):
    with open(os.path.join(BASE_DIR, 'team_payload.json')) as f:
        data = json.load(f)
    response = test_client_with_db.post('/teams/', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 201
    resp_data = json.loads(response.data)
    assert resp_data.get('name') == data.get('name')
    get_by_id(test_client_with_db, resp_data.get('id'))


def test_fails_create_duplicate(test_client_with_db):
    data = {'name': 'South Africa'}
    response = test_client_with_db.post('/teams/', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 419
    resp_data = json.loads(response.data)
    assert 'already exists' in resp_data.get('message')
