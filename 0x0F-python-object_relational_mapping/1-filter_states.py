#!/usr/bin/python3
"""
    Get the states begin by N of a data base
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
    command = """SELECT *
                 FROM states
                 WHERE states.name LIKE BINARY 'N%'
                 ORDER BY states.id ASC"""
    numrows = c.execute(command)
    states = c.fetchall()
    for idstate in states:
        print(idstate)

if __name__ == "__main__":
    main()
