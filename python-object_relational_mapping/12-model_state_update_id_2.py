#!/usr/bin/python3
"""Script that changes the name of a State object from the database"""


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """
    Updates a State object on the database.
    """

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)
    Session = sessionmaker(engine)

    session = Session()

    state = session.query(State).filter(State.id == '2').first()
    state.name = 'New Mexico'
    session.commit()
