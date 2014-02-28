#!/usr/bin/env python
"""
   exercise.py <URL>
      stores JSON object from URL into a mysql db
      JSON format {'name': '', 'id': 0, 'value': '', 'timestamp': '' }

Assumption of Table Name and Columns
mysql> describe json_output;
+-----------+------------------+------+-----+---------+-------+
| Field     | Type             | Null | Key | Default | Extra |
+-----------+------------------+------+-----+---------+-------+
| name      | varchar(25)      | YES  |     | NULL    |       |
| value     | varchar(100)     | YES  |     | NULL    |       |
| timestamp | datetime         | YES  |     | NULL    |       |
| id        | int(10) unsigned | NO   | MUL | NULL    |       |
+-----------+------------------+------+-----+---------+-------+
"""
__author__ = 'eric sales'
__email__ = 'esoupy@gmail.com'

import sys
import json
import urllib2
# import Oracle's mysql python connector
import mysql.connector

# MySQL database info
DATABASE = { 
        'host': 'localhost',
        'database': 'testdb',
        'user': 'user',
        'password': 'passwd',
        'raise_on_warnings': True,
}

# Make sure we get passwd an arg
try:
    url_arg = sys.argv[1]
except IndexError:
    print "missing arg"
    sys.exit(1)

# sql command - we assume table name is json_output
sql_cmd = ( "INSERT INTO json_output " "(name, id, value, timestamp) "
             "VALUES ('%(name)s', '%(id)s', '%(value)s', '%(timestamp)s')" )


# pull the data from restful call
json_data = json.load(urllib2.urlopen(url_arg))

# connect to database
db = mysql.connector.connect(**DATABASE)
db_cursor = db.cursor()

# Insert data
db_cursor.execute(sql_cmd % json_data)
db.commit()

# close db connection
db_cursor.close()
db.close()


