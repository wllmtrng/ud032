import json

def insert_data(data, db):
    for entry in data:
        db.arachnid.insert(entry)


if __name__ == "__main__":
    import os
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017")
    db = client.examples

    with open('arachnid.json') as f:
        data = json.loads(f.read())
        insert_data(data, db)
        print db.arachnid.find_one()
