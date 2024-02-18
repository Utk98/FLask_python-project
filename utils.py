import json
from models import Event, EventEncoder

def load_events():
    try:
        with open('data/events.json', 'r') as file:
            events_data = json.load(file)
            return [Event(**event_data) for event_data in events_data]
    except FileNotFoundError:
        return []

def save_events(events):
    with open('data/events.json', 'w') as file:
        json.dump(events, file, cls=EventEncoder)
