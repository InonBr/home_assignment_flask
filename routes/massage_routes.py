from main import app
from flask_pydantic import validate
from flask_cors import cross_origin
from models import NewMassage
from middleware import auth_required
from flask import request, jsonify
from flask_pymongo import PyMongo
from utils import find_msg_and_update

import os
import uuid

db = os.getenv("MONGODB_KEY")

app.config['MONGO_URI'] = db
mongo = PyMongo(app)

CONTENT_COLLECTIONS = mongo.db.massages


@app.route("/api/createMassage", methods=["POST"])
@cross_origin()
@validate(body=NewMassage)
@auth_required
def create_massage(body: NewMassage):
    massage = body.dict()
    current_user = request.current_user
    massage["_id"] = uuid.uuid4().hex
    CONTENT_COLLECTIONS.insert(massage)

    return {"msg": "massage sent successfully!"}, 201


@app.route("/api/getMassages/<user_id>", methods=["GET"])
@cross_origin()
@auth_required
def get_all_massages(user_id):
    current_user = request.current_user

    if current_user["_id"] != user_id:
        return {"msg": "invalid request"}, 400

    massages_list = list(CONTENT_COLLECTIONS.find({"receiver": current_user["email"]}))

    return jsonify(massages_list)


@app.route("/api/getUnreadMassages/<user_id>", methods=["GET"])
@cross_origin()
@auth_required
def get_unread_massages(user_id):
    current_user = request.current_user

    if current_user["_id"] != user_id:
        return {"msg": "invalid request"}, 400

    massages_list = list(CONTENT_COLLECTIONS.find({"receiver": current_user["email"], "read": False}))

    return jsonify(massages_list)


@app.route("/api/getMassages/<user_id>/<msg_id>", methods=["GET"])
@cross_origin()
@auth_required
def get_a_massage(user_id, msg_id):
    current_user = request.current_user

    if current_user["_id"] != user_id:
        return {"msg": "invalid request"}, 400

    massages = find_msg_and_update(current_user, msg_id)

    if massages is not None:
        return jsonify(massages)

    else:
        return {"msg": "massage not found"}, 400
