#!/usr/bin/python3
"""
lists all states with a name starting with N (upper N) from the database
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    u_name = argv[1]
    p = argv[2]
    db_name = argv[3]
    """lists all states from the database hbtn_0e_0_usa"""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=u_name, passwd=p,
                         db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")

    rows = cur.fetchall()
    for row in rows:
        if row[1][0] == 'N':
            print(row)
    cur.close()
    db.close()
