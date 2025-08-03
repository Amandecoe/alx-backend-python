import sqlite3

class DatabaseConnection:
  def __enter__(conn,query):
   try:
    conn = sqlite3.connect('usersin.db')
    cur = conn.cursor()
    cur.execute(query)
    conn.commit() 
   except sqlite3.Error as b:
    print("Can not open database")
  def __exit__(conn):
   try:
    conn = sqlite3.connect('usersin.db')
   except sqlite3.Error as c:
    print ("Can not close connection")
   finally:
    conn.close() 
try:
     