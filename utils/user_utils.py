from flask_pymongo import PyMongo
from dotenv import load_dotenv
from main import app

import os
import bcrypt

load_dotenv()

db = os.getenv("MONGODB_KEY")

app.config['MONGO_URI'] = db
mongo = PyMongo(app)

CONTENT_COLLECTIONS = mongo.db.users


def insert_user_to_db(new_user):
    new_user = hash_password(new_user)
    CONTENT_COLLECTIONS.insert(new_user)
    del new_user["password"]
    return new_user


# bcrypt users password before saving in the db
def hash_password(new_user):
    new_user["password"] = new_user["password"].encode("utf-8")
    new_user["password"] = bcrypt.hashpw(
        new_user["password"], bcrypt.gensalt(10)
    )

    del new_user["password_repeat"]

    return new_user
