#!/usr/bin/env python3
"""update topics by the name"""


def update_topics(mongo_collection, name, topics):
    """update topics by the name"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
