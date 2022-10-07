#!/usr/bin/python3

"""
File: 100-relationship_states_cities.py
Desc: This module contains a python script that creates the State
“California” with the City “San Francisco” from the database hbtn_0e_100_usa

Author: Gizachew Bayness (Elec Crazy)
Date Created: Oct 7 2022
"""

from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = City(name="San Francisco", state=State(name="California"))
    session.add(state)
    session.commit()
