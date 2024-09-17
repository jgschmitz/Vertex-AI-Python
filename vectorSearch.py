import pymongo
import numpy as np

def perform_vector_search():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["my_database"]
    collection = db["embeddings"]

    # Example: Find vectors close to a given vector
    query_vector = np.array([0.1, 0.5, 0.7])

    # MongoDB $near operator for vector search (requires an index)
    results = collection.find({
        "embedding": {
            "$near": {
                "$geometry": {
                    "type": "Point",
                    "coordinates": query_vector.tolist()
                },
                "$maxDistance": 5
            }
        }
    })

    for result in results:
        print(result)

perform_vector_search()
