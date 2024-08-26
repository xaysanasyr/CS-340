
# Revised
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, user, password, host, port):
        # Connection Variables
        USER = user
        PASS = password
        HOST = host
        PORT = port
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient(f'mongodb://{USER}:{PASS}@{HOST}:{PORT}')
        self.database = self.client[DB]
        self.collection = self.database[COL]

    # Create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            insert_result = self.collection.insert_one(data)
            return insert_result.inserted_id  # Returning the ID of the inserted document
        else:
            raise ValueError("Data is empty")  # Using ValueError for more specificity

    # Read method to implement the R in CRUD.
    def read(self, query):
        if query is not None:
            results = self.collection.find(query)
            return list(results)  # Returning the results as a list of documents
        else:
            raise ValueError("Query is empty")
            
    # Update method
    def update(self, query, update_values):
        if query is not None and update_values is not None:
            result = self.collection.update_many(query, {'$set': update_values})
            return result.modified_count
        else:
            raise ValueError("Query values is empty")
    
    # Delete Method
    
    def delete(self,query):
        if query is not None:
            result = self.collection.delete_many(query)
            return result.deleted_count
        else:
            raise ValueError("Query values is empty")
        
            
