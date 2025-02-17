#first importing the sqlite3 if not
# available run in the terminal pip install sqlite3
import sqlite3
#This is creating a connection to new database named consumer
conn=sqlite3.connect('consumer.db')
#we need to commit (ensuring the request is submitted
conn.commit()
#Finally we need to close connection
conn.close()