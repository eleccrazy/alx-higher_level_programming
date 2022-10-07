#!/usr/bin/python3

"""
File: 3-my_safe_filter_states.py
Desc: This module contains a python script that takes in arguments
and displays all values in the states table of hbtn_0e_0_usa where
name matches the argument.

Author: Gizachew Bayness (Elec Crazy)
Date Created: Oct 7 2022
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )

    cur = db.cursor()
    cur.execute("""SELECT * FROM states ORDER BY id ASC""")
    states_info = cur.fetchall()

    for state in states_info:
        if (state[1] == argv[4]):
            print(state)
