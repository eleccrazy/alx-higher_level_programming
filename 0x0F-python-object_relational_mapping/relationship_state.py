#!/usr/bin/python3

"""
File: relationship_state.py
Desc: This module contains a python script that contains the
class definition of a State and an instance Base = declarative_base()

Author: Gizachew Bayness (Elec Crazy)
Date Created: Oct 7 2022
"""

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from relationship_city import City, Base


class State(Base):
    """
    This class Inherits from Base and links to the MySQL table states.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
