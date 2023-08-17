#!/usr/bin/python3
""" A script that flters states by user input
from database 'hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Getting states from database.
    """

    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)

    curs = db.cursor()
    curs.execute("SELECT * FROM states \
                  WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(argv[4]))
    rows_selected = curs.fetchall()

    for row in rows_selected:
        print(row)

    db.close()
