#!/usr/bin/env python3
"""rite a Python function that lists
all documents in a collection"""


def list_all(mongo_collection):
    """Write a Python function that lists all documents in a collection"""
    list_documents = []
    docs = mongo_collection.find()
    for doc in docs:
        list_documents.append(doc)
    return list_documents
