#!/usr/bin/python3
"""Deletes all State objects that contain the letter 'a' from the databse"""


from model_state import Base, State
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
    Base.metadata.create_all(engine)
    for states in session.query(State).filter(State.name.contains('a')):
        session.delete(states)
    session.commit()
