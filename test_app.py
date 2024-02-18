import json
from datetime import datetime, timedelta
from app import app
from models import Event

# Mocking the data folder path
app.config['DATA_FOLDER'] = 'tests/data/'

def test_get_events_empty():
    response = app.test_client().get('/events')
    assert response.status_code == 200
    assert json.loads(response.data) == {'events': []}

def test_add_event():
    event_data = {
        'title': 'Test Event',
        'description': 'This is a test event',
        'start_time': '2024-02-18T14:00:00',
        'end_time': '2024-02-18T15:00:00'
    }
    response = app.test_client().post('/events', json=event_data)
    assert response.status_code == 201
    assert json.loads(response.data) == {'event': event_data}

def test_get_events_after_adding():
    response = app.test_client().get('/events')
    assert response.status_code == 200
    events = json.loads(response.data)['events']
    assert len(events) == 1
    assert events[0]['title'] == 'Test Event'

def test_update_event():
    updated_event_data = {
        'title': 'Updated Test Event',
        'description': 'This is an updated test event',
        'start_time': '2024-02-18T16:00:00',
        'end_time': '2024-02-18T17:00:00'
    }
    response = app.test_client().put('/events/1', json=updated_event_data)
    assert response.status_code == 200
    assert json.loads(response.data) == {'event': updated_event_data}

def test_delete_event():
    response = app.test_client().delete('/events/1')
    assert response.status_code == 200
    assert json.loads(response.data) == {'message': 'Event deleted successfully'}

def test_get_events_after_deleting():
    response = app.test_client().get('/events')
    assert response.status_code == 200
    assert json.loads(response.data) == {'events': []}

def test_invalid_event_id():
    response = app.test_client().get('/events/999')
    assert response.status_code == 404
    assert json.loads(response.data) == {'error': 'Event not found'}

def test_invalid_update_event_id():
    response = app.test_client().put('/events/999', json={})
    assert response.status_code == 404
    assert json.loads(response.data) == {'error': 'Event not found'}
