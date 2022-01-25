from pymongo import MongoClient
from flask import Flask, jsonify
from bson.json_util import ObjectId
import json

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    
    class JSONEncoder(json.JSONEncoder):

        def default(self, o):
            if isinstance(o, ObjectId):
                return str(o)
            return json.JSONEncoder.default(self, o)


    cluster = MongoClient("mongodb+srv://admin:root@cluster0.vno2z.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster["sample_restaurants"]
    collection = db["restaurants"]
    app.json_encoder = JSONEncoder

    with app.test_request_context():
        results = collection.find_one({"name":"Riviera Caterer"})

        JSONEncoder().encode(results["address"])
        return(results["address"])
    
        # print(jsonify(results["address"]).response)
        
if __name__ == '__main__':
    # This is used when running locally only.
    app.run(host='127.0.0.1', port=8080, debug=True)