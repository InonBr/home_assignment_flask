from flask import request, jsonify
from functools import wraps
from dotenv import load_dotenv
from flask_pymongo import PyMongo
from main import app

import os
import jwt

load_dotenv()

db = os.getenv("MONGODB_KEY")
token = os.getenv("TOKEN")

app.config['MONGO_URI'] = db
mongo = PyMongo(app)

CONTENT_COLLECTIONS = mongo.db.users


def auth_required(f):
    @wraps(f)
    def decode(*args, **kwargs):
        token_test = request.headers.get("Authorization")
        try:
            if token_test is not None:
                current_user = jwt.decode(token_test, token, algorithms=["HS256"])
                email_test = CONTENT_COLLECTIONS.find_one({"email": current_user["email"]})
                # set current user in body
                request.json["current_user"] = email_test

            else:
                return jsonify({'msg': 'Token was not provided!'}), 403

        except jwt.exceptions.DecodeError:
            return jsonify({'msg': 'Token is invalid!'}), 403

        # request.json["current_user"] = "i am awesome"
        # current_user = "I am awesome"
        # print(current_user)
        # current_user.replace("Basic", "I am awesome!!!")
        # print(current_user)
        # print(request.json)
        # request.headers["Authorization"] = "i am awesome"

        # request.headers = {'some_Data': 'i am awesome'}

        # request.json["current_user"] = {"msg": "I am awesome!"}

        return f(*args, **kwargs)

    return decode
