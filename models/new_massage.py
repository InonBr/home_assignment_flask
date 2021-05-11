from pydantic import BaseModel, EmailStr, validator
from utils import get_date_time
from flask_pymongo import PyMongo
from main import app

import os

db = os.getenv("MONGODB_KEY")

app.config['MONGO_URI'] = db
mongo = PyMongo(app)

CONTENT_COLLECTIONS = mongo.db.users


class NewMassage(BaseModel):
    sender: EmailStr
    receiver: EmailStr
    message: str
    subject: str
    read: bool = False
    creation_date: str = get_date_time()

    # validate that the receiver is in the db
    @validator('receiver', pre=True, always=True, allow_reuse=True, check_fields=False)
    def email_validation(cls, v, values):
        email_test = CONTENT_COLLECTIONS.find_one({"email": v})

        if email_test is None:
            raise ValueError("sorry, email does not appear in our list")

        return v
