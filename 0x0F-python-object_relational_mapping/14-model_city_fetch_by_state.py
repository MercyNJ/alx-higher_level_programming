#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa.
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))

    Session = sessionmaker(bind=engine)
    session = Session()

    res = session.query(City, State).join(State)

    for city, state in res.all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()