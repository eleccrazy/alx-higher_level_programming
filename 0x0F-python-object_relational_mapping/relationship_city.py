#!/usr/bin/python3

"""
File: relationship_city.py
Desc: This module contains a python script same as model_city.py

Author: Gizachew Bayness (Elec Crazy)
Date Created: Oct 7 2022
"""

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class City(Base):
    """
    This class Inherits from Base and links to the MySQL table cities.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
