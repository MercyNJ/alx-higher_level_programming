#!/usr/bin/python3
""" A script that safely filters states by user
input from database 'hbtn_0e_0_usa`.
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
    search_name = argv[4]

    db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database,
            port=3306
            )

    curs = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    curs.execute(query, (search_name,))

    rows_selected = curs.fetchall()

    for row in rows_selected:
        print(row)

    db.close()
