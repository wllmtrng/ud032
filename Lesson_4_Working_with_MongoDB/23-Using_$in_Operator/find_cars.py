#!/usr/bin/env python
""" Your task is to write a query that will return all cars manufactured by "Ford Motor Company"
that are assembled in Germany, United Kingdom, or Japan.
Please modify only 'in_query' function, as only that will be taken into account.

Your code will be run against a MongoDB instance that we have provided.
If you want to run this code locally on your machine,
you have to install MongoDB, download and insert the dataset.
For instructions related to MongoDB setup and datasets please see Course Materials.
"""

def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.examples
    return db


def in_query():
    # Write the query
    query = {"manufacturer": "Ford Motor Company",
             "assembly": {"$in": ["Germany", "United Kingdom", "Japan"]}}

    return query


if __name__ == "__main__":

    db = get_db()
    query = in_query()
    autos = db.autos.find(query, {"name":1, "manufacturer":1, "assembly": 1, "_id":0})

    print "Found autos:", autos.count()
    import pprint
    for a in autos:
        pprint.pprint(a)

"""
Found autos: 17
Printing first 3 results

{u'assembly': [u'Argentina',
               u'Australia',
               u'Berlin',
               u'Brazil',
               u'Buenos Aires',
               u'Canada',
               u'Copenhagen',
               u'Cork',
               u'Denmark',
               u'Detroit',
               u'Dothan Alabama',
               u'England',
               u'Geelong',
               u'Germany',
               u'Highland Park Michigan',
               u'Ireland',
               u'Manchester',
               u'Minneapolis',
               u'Ontario',
               u'S\xe3o Bernardo do Campo',
               u'Saint Paul Minnesota',
               u'Toronto',
               u'Walkerville Ontario'],
 u'manufacturer': u'Ford Motor Company',
 u'name': u'Ford Model T'}
{u'assembly': [u'Chongqing',
               u'Germany',
               u'Michigan Assembly Plant',
               u'Rayong',
               u'Russia',
               u'Saarlouis Body & Assembly',
               u'Thailand',
               u'United States',
               u'Vsevolozhsk'],
 u'manufacturer': u'Ford Motor Company',
 u'name': u'Ford Focus'}
{u'assembly': [u'Australia',
               u'Hiroshima',
               u'Homebush New South Wales',
               u'Japan',
               u'New Zealand',
               u'Pretoria',
               u'South Africa',
               u'Taiwan'],
 u'manufacturer': u'Ford Motor Company',
 u'name': u'Ford Telstar'}
 """
