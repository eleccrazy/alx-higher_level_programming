#!/usr/bin/python3

"""
File: model_city.py
Desc: This module contains a python script that contains the
class definition of a City.

Author: Gizachew Bayness (Elec Crazy)
Date Created: Oct 7 2022
"""

from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import Base


class City(Base):
    """
    This class Inherits from Base and links to the MySQL table cities.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
