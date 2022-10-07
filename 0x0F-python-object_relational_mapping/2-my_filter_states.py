#!/usr/bin/python3

"""
File: 2-my_filter_states.py
Desc: This module takes in an argument and displays all
values in the states table of hbtn_0e_0_usa where name
matches the argument.

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
    cur.execute("""SELECT * FROM states
            WHERE BINARY name='{}'
            ORDER BY id ASC""".format(argv[4]))
    states_info = cur.fetchall()

    for state in states_info:
        print(state)
