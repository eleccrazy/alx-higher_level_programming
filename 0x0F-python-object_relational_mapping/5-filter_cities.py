#!/usr/bin/python3

"""
File: 5-filter_cities.py
Desc: This module contains a python script that takes in the
name of a state as an argument and lists all cities of that
state, using the database hbtn_0e_4_usa

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
    cur.execute("""SELECT cities.id, cities.name,
            states.name FROM cities
            INNER JOIN states
            ON cities.state_id = states.id
            ORDER BY cities.id ASC""")
    states_info = cur.fetchall()

    filtered_list_state = ([state[1] for state in states_info
                            if state[2] == argv[4]])
    print(", ".join(filtered_list_state))
