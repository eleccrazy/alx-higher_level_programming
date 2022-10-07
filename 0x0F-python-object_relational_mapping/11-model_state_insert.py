#!/usr/bin/python3

"""
File: 11-model_state_insert.py
Desc: This module contains a python script that adds the
State object “Louisiana” to the database hbtn_0e_6_usa

Author: Gizachew Bayness (Elec Crazy).
Date Created: Oct 7 2022
"""

from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    louisiana = State(name="Louisiana")
    session.add(louisiana)
    session.commit()
    session.refresh(louisiana)
    print(louisiana.id)
