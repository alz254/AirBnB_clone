#!/usr/bin/python3
"""
Module City class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Inherits from BaseModel
    Public class attribute:
        state_id: (str)
        name: (str)
    """
    state_id=""
    name = ""
