#!/usr/bin/python3

"""
File: 12-model_state_update_id_2.py
Desc: This module contains a python script that changes the
name of a State object from the database hbtn_0e_6_usa

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

    state = session.query(State).filter(State.id == 2).first()
    state.name = "New Mexico"
    session.commit()
