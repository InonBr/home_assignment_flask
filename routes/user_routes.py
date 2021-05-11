from main import app
from flask_pydantic import validate
from flask_cors import cross_origin
from models import User
from utils import insert_user_to_db

import uuid


@app.route("/api/createUser", methods=["POST"])
@cross_origin()
@validate(body=User)
def create_user(body: User):
    new_user = body.dict()
    new_user["_id"] = uuid.uuid4().hex
    new_user = insert_user_to_db(new_user)

    return {"user": new_user, "msg": "new user created successfully!"}, 200
