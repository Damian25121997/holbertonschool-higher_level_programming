#!/usr/bin/python3
"""The script lists all states from the database"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    """Access to the database"""
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    curs = db.cursor()
    curs.execute("SELECT cities.id, cities.name, states.name\
                  FROM cities JOIN states\
                  ON cities.state_id = states.id\
                  ORDER BY cities.id ASC")
    rows = curs.fetchall()

    for row in rows:
        print(row)
