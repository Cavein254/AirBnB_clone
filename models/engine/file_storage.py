from datetime import datetime
import json
import os

from ..base_models import BaseModel
class FileStorage:
    def __init__(self, file_path="storage.json"):
        self.file_path = file_path
        self.objects = {}

    def save(self):
        data = {}
        for key, value in self.objects.items():
            data[key] = json.loads(value.to_json())

        with open(self.file_path, 'w') as file:
            json.dumps(data, file) 

    def reload(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    obj = BaseModel(**value)
                    self.objects[key] = obj

    def add_object(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.objects[key] = obj

if __name__ == "__main__":
    storage = FileStorage()

    base_model_instance = BaseModel()
    storage.add_object(base_model_instance)
    storage.reload()
    reloaded_instance = storage.objects.get("BaseModel.1")

    if reloaded_instance:
        print(reloaded_instance.to_json())