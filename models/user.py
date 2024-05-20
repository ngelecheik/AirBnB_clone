#!/usr/bin/python3
'holds the class user that inherits from base model'
from models.base_model import BaseModel


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
