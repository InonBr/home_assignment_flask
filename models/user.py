from pydantic import BaseModel, EmailStr, Field, validator
from utils import get_date_time
from flask_pymongo import PyMongo
from main import app

import os

db = os.getenv("MONGODB_KEY")

app.config['MONGO_URI'] = db
mongo = PyMongo(app)

CONTENT_COLLECTIONS = mongo.db.users


class User(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6)
    password_repeat: str
    date_time: str = get_date_time()

    # validate that email is unique
    @validator('email', pre=True, always=True, allow_reuse=True)
    def email_validation(cls, v, values):
        email_test = CONTENT_COLLECTIONS.find_one({"email": v})

        if email_test is not None:
            raise ValueError("email already exist")

        return v

    # test if passwords are matching
    @validator('password_repeat', pre=True, always=True, allow_reuse=True)
    def passwords_match(cls, v, values):
        if 'password' in values and v != values['password']:
            raise ValueError('passwords do not match')
        return v
