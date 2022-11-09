#!/usr/bin/python3
"""Prints all City objects that from the databse"""


from model_state import Base, State
from model_city import City
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """Access the database"""
    db = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
         argv[1], argv[2], argv[3])
    engine = create_engine(db)
    Session = sessionmaker(engine)
    session = Session()

    states = session.query(City, State).join(State)
    for c, s in states.all():
        print("{}: ({}) {}".format(s.name, c.id, c.name))
    session.commit()
    session.close()
