#!/usr/bin/env python3
"""returns all students sorted by score"""


def top_students(mongo_collection):
    """ List all students sorted by score """
    return mongo_collection.aggregate([
        {
            '$project': {
                'name': '$name',
                'averageScore': {
                    '$avg': "$topics.score"
                }
            }
        },
        {
            '$sort': {
                "averageScore": -1
            }
        }
    ])
