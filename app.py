from flask import Flask, jsonify, request
from models import Event, EventEncoder
import json
from utils import load_events, save_events

app = Flask(__name__)
events = load_events()

@app.route('/events', methods=['GET'])
def get_events():
    sorted_events = sorted(events, key=lambda x: x.start_time)
    return jsonify({'events': sorted_events})

@app.route('/events', methods=['POST'])
def add_event():
    new_event_data = request.get_json()
    new_event = Event(**new_event_data)
    events.append(new_event)
    save_events(events)
    return jsonify({'event': new_event_data}), 201

# Implement other routes for updating and deleting events

if __name__ == '__main__':
    app.run(debug=True)
