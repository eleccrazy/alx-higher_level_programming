#!/usr/bin/python3

"""
File: 1-filter_states.py
Desc: This module contains a script that  lists all states
with a name starting with N (upper N) from the database hbtn_0e_0_usa

Author: Gizachew Bayness (Elec Crazy)
Date Created: Oct 7, 2022
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
            WHERE BINARY name LIKE 'N%'
            ORDER BY id ASC""")
    states_info = cur.fetchall()

    for state in states_info:
        print(state)
