# compose_flask/app.py
from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId
from flask_cors import CORS
import json
import sys


app = Flask(__name__)
client = MongoClient('mongodb://root:root@mongo:27017')
db = client.db
users = db.users
CORS(app)

@app.route('/create', methods=['GET'])
def create():
    if 'user' in request.args and 'pwd' in request.args:
        user = request.args['user']
        pwd = request.args['pwd']
        result = users.insert_one({
            'user': str(user),
            'pwd': str(pwd)
        })
    else:
        return "Error: No id field provided. Please specify an id.", 500
    
    return "OK", 200

@app.route('/login', methods=['GET'])
def login():
    if 'user' in request.args and 'pwd' in request.args:
        usr = request.args['user']
        found_usr = users.find_one({'user':usr})
        if found_usr != None and found_usr['pwd'] == request.args['pwd']:
            return "OK", 200
    
    return "NO", 500



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
