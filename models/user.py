from pydantic import BaseModel, EmailStr, Field, validator
from utils import get_date_time
from typing import Optional


class User(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6)
    password_repeat: str
    date_time: str = get_date_time()

    @validator('password_repeat', pre=True, always=True, allow_reuse=True)
    def passwords_match(cls, v, values):
        if 'password' in values and v != values['password']:
            raise ValueError('passwords do not match')
        return v
