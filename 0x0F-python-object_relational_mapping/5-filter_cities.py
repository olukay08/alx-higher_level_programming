#!/usr/bin/python3
"""
    Get the cities of 1 state of a database
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
    command = """SELECT cities.name
                 FROM cities, states
                 WHERE BINARY states.name = %s
                 AND cities.state_id = states.id
                 ORDER BY cities.id ASC"""
    numrows = c.execute(command, (argv[4],))
    states = c.fetchall()
    print(", ".join(citistate[0] for citistate in states))

if __name__ == "__main__":
    main()
