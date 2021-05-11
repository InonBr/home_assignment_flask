from pydantic import BaseModel, EmailStr, validator
from flask_pymongo import PyMongo
from main import app

import os

db = os.getenv("MONGODB_KEY")

app.config['MONGO_URI'] = db
mongo = PyMongo(app)

CONTENT_COLLECTIONS = mongo.db.users


class UserLogin(BaseModel):
    email: EmailStr
    password: str

    # validate that email is existing in the db
    @validator('email', pre=True, always=True, allow_reuse=True)
    def existing_email(cls, v, values):
        email_test = CONTENT_COLLECTIONS.find_one({"email": v})

        if email_test is None:
            raise ValueError("wrong credentials")

        values["current_user"] = email_test

        return v

