#!/usr/bin/python3
'holds the class Review that inherits from base model'
from models.base_model import BaseModel


class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""
