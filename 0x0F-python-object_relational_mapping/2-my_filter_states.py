#!/usr/bin/python3

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
            WHERE name='{}'
            ORDER BY id ASC""".format(argv[4]))
    states_info = cur.fetchall()

    for state in states_info:
        print(state)
