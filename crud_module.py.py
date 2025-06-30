#!/usr/bin/env python
# coding: utf-8

# In[1]:


# crud_module.py

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    def __init__(self, username, password):
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31580
        DB = 'aac'
        COL = 'animals'
        self.client = MongoClient(f"mongodb://{username}:{password}@{HOST}:{PORT}/?authSource=admin")
        self.database = self.client[DB]
        self.collection = self.database[COL]

    def create(self, data):
        if data:
            self.collection.insert_one(data)
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    def read(self, query={}):
        return list(self.collection.find(query))

    def update(self, query, new_values):
        if query and new_values:
            result = self.collection.update_many(query, {"$set": new_values})
            return result.modified_count
        else:
            raise Exception("Missing query or new values")

    def delete(self, query):
        if query:
            result = self.collection.delete_many(query)
            return result.deleted_count
        else:
            raise Exception("Missing query parameter")


# In[ ]:




