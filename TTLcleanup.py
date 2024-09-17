import pymongo
from datetime import datetime, timedelta

def delete_old_records():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["my_database"]
    collection = db["logs"]

    # Define the time threshold (e.g., delete data older than 30 days)
    threshold = datetime.now() - timedelta(days=30)

    # Delete old records
    result = collection.delete_many({"timestamp": {"$lt": threshold}})

    print(f"Deleted {result.deleted_count} old records.")

delete_old_records()
