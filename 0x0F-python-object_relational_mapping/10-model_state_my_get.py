#!/usr/bin/python3
"""
Lists s specified State object passed as
an arg from the database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_to_search = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))

    Session = sessionmaker(bind=engine)
    session = Session()

    query = (session.query(State)
             .filter(State.name == state_to_search)
             )
    res = query.first()

    if res is None:
        print("Not found")
    else:
        print(res.id)

    session.close()
