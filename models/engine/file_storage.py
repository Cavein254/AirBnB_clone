#!/usr/bin/python3
from datetime import datetime
import json
import os

from models.base_model import BaseModel
from models.user import User

class FileStorage:
    __objects = {}
    __file_path="file.json"

    def new(self, obj):
        obj_name = obj.__class__.__name__
        key = "{}.{}".format(obj_name, obj.id)
        FileStorage.__objects[key] = obj
    
    def all(self):

        return FileStorage.__objects

    def save(self):
        data = {}
        all_objs = FileStorage.__objects
        for key in all_objs.keys():
            data[key] = all_objs[key].to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(data, file) 

    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                try:
                    data = json.load(file)
                    for key in data.values():
                        class_name = key["__class__"]
                        del key["__class__"]
                        self.new(eval(class_name)(**key))
                        print(FileStorage.__objects)
                except Exception:
                    pass
                

# if __name__ == "__main__":
#     storage = FileStorage()
#     base_model_instance = BaseModel()
#     storage.add_object(base_model_instance)
#     storage.reload()
#     reloaded_instance = storage.objects.get("BaseModel.1")

#     if reloaded_instance:
#         print(reloaded_instance.to_json())