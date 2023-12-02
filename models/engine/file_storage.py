#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return list(FileStorage.__objects.values())
        else:
            return [obj for obj in FileStorage.__objects.values() if isinstance(obj,cls)]

    def delete(self, obj=None):
        """Deletes an object from the storage"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]

    def new(self, obj):
        """Adds new object to storage dictionary"""
       ## self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
            temp = {}
            for key, obj in FileStorage.__objects.items():
                temp[key] = obj.to_dict()
                with open(FileStorage.__file_path, 'w') as file:
            json.dump(temp, file)

    def close(self):
        """Method for closing Flask connection"""
        self.reload()

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                temp = json.load(file)
                for key, value in temp.items():
                    cls_name = value['__class__']
                    cls = eval(cls_name)
                    obj = cls(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
