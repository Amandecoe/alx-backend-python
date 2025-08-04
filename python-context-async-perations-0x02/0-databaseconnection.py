import sqlite3

class DatabaseConnection:
  def __enter__(self):  #is used to open the connection
   try:
    self.conn = sqlite3.connect('usersin.db')
    print ("Database opened succesfully")
   except sqlite3.Error as b:
    print("Can not open database")
  def __exit__(self,exc_type, exc_val, exc_tb): # is used to close the connection
   try:
    conn = sqlite3.connect('usersin.db')
    print ("database closed")
   except sqlite3.Error as c:
    print ("Can not close connection")
   finally:
    conn.close() 
try:
 with sqlite3.connect('usersin.db') as conn:
  cursor=conn.cursor()
  cursor.execute('SELECT * FROM users')
  result = cursor.fetchall()
except sqlite3.Error as c:
 print ("Error executing query")   


     