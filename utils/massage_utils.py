from main import app
from flask_pymongo import PyMongo
from dotenv import load_dotenv

import os

load_dotenv()

db = os.getenv("MONGODB_KEY")

app.config['MONGO_URI'] = db
mongo = PyMongo(app)

CONTENT_COLLECTIONS = mongo.db.massages


def find_msg_and_update(current_user, msg_id):
    CONTENT_COLLECTIONS.update_one({"receiver": current_user["email"], "_id": msg_id},
                                   {"$set": {"read": True}})

    massages = CONTENT_COLLECTIONS.find_one({"receiver": current_user["email"], "_id": msg_id})

    return massages
