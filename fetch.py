from pymongo import MongoClient

def connect_to_mongodb(connection_string):
    client = MongoClient(connection_string)
    return client

def fetch_data_from_mongodb(database_name, collection_name, client):
    db = client[database_name]
    collection = db[collection_name]
    
    # Customize the query based on your data structure
    data = list(collection.find({}))
    
    return data
