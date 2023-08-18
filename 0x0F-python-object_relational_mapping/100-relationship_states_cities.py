#!/usr/bin/python3
"""
Creates specified states with its associated
city in the the database hbtn_0e_14_usa.
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    california_state = State(name='California')
    san_francisco_city = City(name='San Francisco')
    california_state.cities.append(san_francisco_city)

    session.add(california_state)
    session.commit()

    session.close()
