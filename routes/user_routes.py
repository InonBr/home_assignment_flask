from main import app
from flask_pydantic import validate
from flask_cors import cross_origin
from models import User, UserLogin
from utils import insert_user_to_db
from dotenv import load_dotenv

import bcrypt
import os
import uuid
import jwt

load_dotenv()

token = os.getenv("TOKEN")


@app.route("/api/createUser", methods=["POST"])
@cross_origin()
@validate(body=User)
def create_user(body: User):
    new_user = body.dict()
    new_user["_id"] = uuid.uuid4().hex
    new_user = insert_user_to_db(new_user)
    # encoding users data before sending it back
    new_user = jwt.encode(new_user, token, algorithm="HS256")

    return {"user": new_user, "msg": "new user created successfully!"}, 201


@app.route("/api/login", methods=["POST"])
@cross_origin()
@validate(body=UserLogin)
def login(body: UserLogin):
    user = body.dict()
    password_compare = user["password"].encode("utf-8")

    if bcrypt.checkpw(password_compare, user["current_user"]["password"]):
        if "password" in user["current_user"]:
            del user["current_user"]["password"]

        encoded_user_data = jwt.encode(user["current_user"], token, algorithm="HS256")

        return {"user": encoded_user_data, "msg": "user loggedin successfully!"}, 200

    else:
        return {"msg": "wrong credentials!"}, 400
