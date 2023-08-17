#!/usr/bin/python3
""" A script that lists all cities
from database 'hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Getting filtered states from database.
    """
    username = argv[1]
    password = argv[2]
    database = argv[3]

    db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database,
            port=3306
            )

    curs = db.cursor()
    curs.execute("SELECT cities.id, cities.name, states.name \
            FROM cities JOIN states ON cities.state_id \
            = states.id ORDER BY cities.id ASC")

    rows_selected = curs.fetchall()

    for row in rows_selected:
        print(row)

    db.close()
