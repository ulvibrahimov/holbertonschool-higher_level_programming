#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
It takes 3 arguments: mysql username, mysql password, and database name.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to a MySQL database running on localhost at port 3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor object to execute queries
    cur = db.cursor()

    # Execute the SQL query to select all states, ordered by id
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows returned by the query
    rows = cur.fetchall()

    # Print each row exactly as formatted by the fetchall output
    for row in rows:
        print(row)

    # Clean up and close the cursor and database connection
    cur.close()
    db.close()
