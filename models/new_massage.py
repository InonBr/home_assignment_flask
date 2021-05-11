from pydantic import BaseModel
from utils import get_date_time


class NewMassage(BaseModel):
    sender: str
    receiver: str
    message: str
    subject: str
    read: bool = False
    creation_date: str = get_date_time()
