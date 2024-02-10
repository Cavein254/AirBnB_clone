import json
from datetime import datetime

class BaseModel():
    def __init__(self, id=None, created_at=None, updated_at=None):
        self.id = id
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()

    def to_json(self):
        return json.dumps({
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        })
    

