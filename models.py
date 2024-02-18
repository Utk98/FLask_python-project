from datetime import datetime
import json


class Event:
    def __init__(self, title, description, start_time, end_time):
        self.title = title
        self.description = description
        self.start_time = datetime.fromisoformat(start_time)
        self.end_time = datetime.fromisoformat(end_time)

class EventEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Event):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)

















































































































































































































































































































































































































































































































































