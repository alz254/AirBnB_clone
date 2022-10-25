#!/usr/bin/python3
"""Defines the city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a City

    Attributes:
        state_id (str): The state id
        name (str): City Name
    """

    state_id = ""
    name = ""
