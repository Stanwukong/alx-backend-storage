#!/usr/bin python3
"""Adds a new document based on input"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a collection based
    on keyword arguments (kwargs).

    Args:
        mongo_collection: The pymongo collection object.
        **kwargs: The keyword arguments representing the
                  fields and values for the new document.

    Returns:
        The _id of the newly inserted document.
    """
    result = mongo_collection.insert_one(kwargs)

    return result.inserted_id
