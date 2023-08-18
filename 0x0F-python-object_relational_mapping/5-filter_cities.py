#!/usr/bin/python3
""" A script that lists all cities of a
specific state from database 'hbtn_0e_0_usa`.
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
    state_name = argv[4]

    db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database,
            port=3306
            )

    curs = db.cursor()
    curs.execute("SELECT cities.name \
            FROM cities JOIN states ON cities.state_id \
            = states.id WHERE states.name = %s \
            ORDER BY cities.id ASC", (state_name,))

    cities_selected = curs.fetchall()

    cities_list = [city[0] for city in cities_selected]
    cities_str = ", ".join(cities_list)
    print(cities_str)

    db.close()
