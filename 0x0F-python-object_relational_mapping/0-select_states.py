#!/usr/bin/python3
"""
file: 0-select_states.py
Desc: This module contains a script to  lists all
states from the database hbtn_0e_0_usa

Author: Gizachew Bayness (Elec Crazy).

Date Created: oct 7, 2022
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
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    states_info = cur.fetchall()

    for state in states_info:
        print(state)
