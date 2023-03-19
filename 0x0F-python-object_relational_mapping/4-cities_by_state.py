#!/usr/bin/python3
"""
    Get all the cities of a data base
"""
import MySQLdb
from sys import argv


def main():
    """Only executes when is not imported"""
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         port=3306,
                         passwd=argv[2],
                         db=argv[3])
    c = db.cursor()
    command = """SELECT cities.id, cities.name, states.name
                 FROM cities, states
                 WHERE cities.state_id = states.id
                 ORDER BY cities.id ASC"""
    numrows = c.execute(command)
    states = c.fetchall()
    for idstate in states:
        print(idstate)

if __name__ == "__main__":
    main()
