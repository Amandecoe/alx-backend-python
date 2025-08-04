import sqlite3

class ExecuteQuery:
  def __init__(self, db_name = 'usersin.db'):
    self.db_name=db_name
  def __enter__(self):
    try:
      self.conn = sqlite3.connect('usersin.db')
      print ("Database Opened Successfuly")
      return self.conn
    except sqlite3.Error as h:
      print("Error Opening Database")
  def __exit__(self, exc_type, exc_val):
    if self.conn:
      try: 
        if exc_type:
          print (f"Error occured: {exc_val}")
          self.conn.rollback()
        else:
          self.conn.commit()   
      except sqlite3.Error as g:
        print ("Error during rollback")
      finally:
        self.conn.close()
        print("Database connection closed succesfully")

if __name__ == '__main__':
  try:
    