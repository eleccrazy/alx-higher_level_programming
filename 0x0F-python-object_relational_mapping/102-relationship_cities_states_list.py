#!/usr/bin/python3

"""
File: 102-relatinship_states_cities_list.py
Desc: This module contains a python script that lists all City
objects from the database hbtn_0e_101_usa

Author: Gizachew Bayness (Elec Crazy)
Date Created: Oct 8 2022
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from relationship_state import State
from relationship_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(City).order_by(City.id)
    for city in result:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
