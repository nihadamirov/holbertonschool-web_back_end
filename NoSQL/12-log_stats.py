#!/usr/bin/env python3
"""Log stats"""
from pymongo import MongoClient

# Connect to MongoDB and select the nginx collection from the logs database
client = MongoClient('mongodb://127.0.0.1:27017')
db = client.logs
nginx_collection = db.nginx

def log_stats():
    """ Function to print statistics about Nginx logs stored in MongoDB """
    
    # Count the total number of documents in the collection
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # Methods statistics
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        # Count the number of documents for each HTTP method
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    
    # Count the number of documents where method is GET and path is /status
    status_check = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")

if __name__ == "__main__":
    log_stats()
